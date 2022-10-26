import os
import logging
from scrapy import Selector
import scrapy
from scrapy.crawler import CrawlerProcess

# scrapy crawl spider1 -o results.json


class QuotesSpider1(scrapy.Spider):
    villes = ["Mont Saint Michel","St Malo","Bayeux","Le Havre","Rouen","Paris","Amiens","Lille","Strasbourg","Chateau du Haut Koenigsbourg","Colmar","Eguisheim","Besancon","Dijon","Annecy","Grenoble","Lyon","Gorges du Verdon","Bormes les Mimosas","Cassis","Marseille","Aix en Provence","Avignon","Uzes","Nimes","Aigues Mortes","Saintes Maries de la mer","Collioure","Carcassonne","Ariege","Toulouse","Montauban","Biarritz","Bayonne","La Rochelle"]
    name = "spider1"
    liste_urls = []
    for ville in villes:
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?ss={ville}&ssne={ville}&ssne_untouched={ville}&label=fr-&lang=fr&&sb=1&src_elem=sb&dest_type=city&checkin=2022-11-21&checkout=2022-11-27")

    start_urls = liste_urls
            
        
    def parse(self, response):
        
        keys = response.css('div.a826ba81c4.fe821aea6c.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942')
        print(keys)
        for key in keys:
            yield {
                "ville": key.css("span.f4bd0794db.b4273d69aa::text").get(),
                "hotel": key.css('div.fcab3ed991::text').get(),
                "url": key.css('a.e13098a59f::attr(href)').get(),
                "note": key.css('div.b5cd09854e.d10a6220b4::text').get() 
            }
        

filename = "resultat.json"

if filename in os.listdir():
        os.remove( filename)
        

process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        filename : {"format": "json"},
    }
})

process.crawl(QuotesSpider1)
process.start()
      

