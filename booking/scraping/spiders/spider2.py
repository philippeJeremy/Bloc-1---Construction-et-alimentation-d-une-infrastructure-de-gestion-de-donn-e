import os
import json
import logging
import scrapy
from scrapy.crawler import CrawlerProcess

# scrapy crawl spider2 -o hotel.json

class QuotesSpider2(scrapy.Spider):
    name = "spider2"
    file = open("resultat.json")
    file = json.load(file)
    liste_urls = [element["url"] for element in file] 

    start_urls = liste_urls
    print(liste_urls)
        
    def parse(self, response):
            
            a = response.css('#hotel_address::attr(data-atlas-latlng)').get(),
            b = a[0]
            c = b.split(",")
            
            yield {
                "hotel": response.css('h2.pp-header__title::text').get(),
                "description" : response.css('#property_description_content > p::text').get(),
                "latitutde": c[0],
                "longitude": c[1],
            }
        
filename = "hotel.json"

if filename in os.listdir():
        os.remove( filename)
        
process = CrawlerProcess(settings = {
    'USER_AGENT': 'Chrome/97.0',
    'LOG_LEVEL': logging.INFO,
    "FEEDS": {
        filename : {"format": "json"},
    }
})

process.crawl(QuotesSpider2)
process.start()







