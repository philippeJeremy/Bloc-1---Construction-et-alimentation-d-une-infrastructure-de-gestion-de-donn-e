import os
import logging
from scrapy import Selector
import scrapy
from scrapy.http import Request, Response, JsonRequest
from scrapy.crawler import CrawlerProcess
import json


# scrapy crawl spider1 -o results.json

class QuotesSpider1(scrapy.Spider):


        
    villes = ["Le Mont-Saint-Michel","St Malo","Bayeux","Le Havre","Rouen","Paris","Amiens","Lille","Strasbourg","Chateau du Haut Koenigsbourg","Colmar","Eguisheim","Besancon","Dijon","Annecy","Grenoble","Lyon","Gorges du Verdon","Bormes les Mimosas","Cassis","Marseille","Aix-en-Provence","Avignon","Uzès","Nimes","Aigues Mortes","Saintes Maries de la mer","Collioure","Carcassonne","Ariege","Toulouse","Montauban","Biarritz","Bayonne","La Rochelle"]
    name = "spider1"
    count = 0
    liste_urls = []
    for ville in villes:
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=0")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=25")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=50")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=75")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=100")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=125")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=150")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=175")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=200")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=225")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=250")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=275")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=300")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=325")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=350")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=375")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=400")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=425")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=450")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=475")
            liste_urls.append(f"https://www.booking.com/searchresults.fr.html?label=gog235jc-1DCAEoggI46AdIDVgDaE2IAQGYAQ24ARfIAQzYAQPoAQH4AQKIAgGoAgO4ArSu-ZoGwAIB0gIkNzBlOWM1Y2ItNDVhYi00OWVkLTg2ZWEtZTJiODhjN2I2YjA32AIE4AIB&aid=397594&ss={ville}&ssne={ville}&ssne_untouched={ville}&lang=fr&sb=1&src_elem=sb&src=searchresults&dest_type=city&checkin=2022-11-21&checkout=2022-11-27&group_adults=2&no_rooms=1&group_children=0&sb_travel_purpose=leisure&offset=500")
            
    

            
    def parse(self, response):
        
        print(response)
        keys = response.css('div.a826ba81c4.fe821aea6c.fa2f36ad22.afd256fc79.d08f526e0d.ed11e24d01.ef9845d4b3.da89aeb942')
        print(keys)
        url_hotels = [] 


        for key in keys:
            recherche = response.css('input.ce45093752::attr(value)').get()
            url_hotel = key.css('a.e13098a59f::attr(href)').get()
            url_hotels.append(url_hotel)
            
            yield {
                "ville_rechercher" : recherche,
                "ville_précise": key.css("span.f4bd0794db.b4273d69aa::text").get(),
                "hotel": key.css('div.fcab3ed991.a23c043802::text').get(),
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
      

