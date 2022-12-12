import os
import scrapy
import logging

from scrapy.crawler import CrawlerProcess

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
        
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        filename : {"format": "json"},
    },
    "AUTOTHROTTLE_ENABLED": True
})

process.crawl(QuotesSpider1)
process.start()