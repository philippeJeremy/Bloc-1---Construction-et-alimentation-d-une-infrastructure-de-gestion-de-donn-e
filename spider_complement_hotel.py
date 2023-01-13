import os
import json
import scrapy
import random
import logging

from scrapy.crawler import CrawlerProcess

# Information complémentaire sur les hôtels
class QuotesSpider2(scrapy.Spider):
    name = "spider2"
    file = open("hotel_1.json")
    file = json.load(file)
    liste_urls = [element["url"] for element in file] 

    start_urls = liste_urls
        
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
        
filename = "hotel_2.json"

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

process.crawl(QuotesSpider2)
process.start()