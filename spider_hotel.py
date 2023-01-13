import os
import scrapy
import random
import logging

from scrapy.crawler import CrawlerProcess

# Récupération des hôtels
class QuotesSpider1(scrapy.Spider):
    name = "spider1"
    start_urls = ['https://www.booking.com/index.fr.html']
    id = 0
    def parse(self, response):
        villes = ["Le Mont-Saint-Michel","St Malo","Bayeux","Le Havre","Rouen","Paris","Amiens","Lille","Strasbourg","Chateau du Haut Koenigsbourg","Colmar","Eguisheim","Besancon","Dijon","Annecy","Grenoble","Lyon","Gorges du Verdon", 
                "Bormes les Mimosas","Cassis","Marseille","Aix-en-Provence","Avignon","Uzès","Nimes","Aigues Mortes","Saintes Maries de la mer","Collioure","Carcassonne","Ariege","Toulouse","Montauban","Biarritz","Bayonne","La Rochelle"]
        
        for x in villes:
            yield scrapy.FormRequest.from_response(
            response,
            formdata={'ss': x },
            callback=self.after_search
        )
        
    def after_search(self, response):
        villes = response.url.split("ss=")[-1].split("&")[0]
        keys = response.css('div.a826ba81c4.fe821aea6c.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942')
        url_hotels = []
        self.id += 1
        for key in keys:
            url_hotel = key.css('a.e13098a59f::attr(href)').get()
            url_hotels.append(url_hotel)
            
            yield {
                "id" : self.id,
                "ville": key.css("span.f4bd0794db.b4273d69aa::text").get(),
                "hotel": key.css('div.fcab3ed991.a23c043802::text').get(),
                "url": key.css('a.e13098a59f::attr(href)').get(),
                "note": key.css('div.b5cd09854e.d10a6220b4::text').get() 
            }
            
        try:
            next_page = response.css('button.fc63351294.f9c5690c58').attrib["href"]
        except KeyError:
            logging.info('No next page. Terminating crawling process.')
        else:
            yield response.follow(next_page, callback=self.after_search)
                            
filename = "hotel_1.json"

if filename in os.listdir():
        os.remove( filename)

user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
    'Chrome/97.0',
]

process = CrawlerProcess(settings = {
    'USER_AGENT': user_agent_list[random.randint(0, len(user_agent_list)-1)],
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        filename : {"format": "json"},
    },
    "AUTOTHROTTLE_ENABLED": True
})

process.crawl(QuotesSpider1)
process.start()