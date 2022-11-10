from bs4 import BeautifulSoup
import requests
from pprint import pprint
import json
import os

headers = {'User-Agent':'Chrome/97.0'}
url = r"https://www.booking.com/searchresults.fr.html?aid=376366&label=fr-shaCYELBNr81MpYUadbCTAS410565919163%3Apl%3Ata%3Ap1%3Ap22.563.000%3Aac%3Aap%3Aneg%3Afi%3Atikwd-33467740%3Alp9108252%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9Ye7BFAsTyVd6vvamF_no64o&sid=f3bcfebb977c2cc20d8dda1cf1d5f60f&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.fr.html%3Faid%3D376366%26label%3Dfr-shaCYELBNr81MpYUadbCTAS410565919163%253Apl%253Ata%253Ap1%253Ap22.563.000%253Aac%253Aap%253Aneg%253Afi%253Atikwd-33467740%253Alp9108252%253Ali%253Adec%253Adm%253Appccp%253DUmFuZG9tSVYkc2RlIyh9Ye7BFAsTyVd6vvamF_no64o%26sid%3Df3bcfebb977c2cc20d8dda1cf1d5f60f%26sb_price_type%3Dtotal%26%26&ss=Paris&is_ski_area=0&ssne=Paris&ssne_untouched=Paris&dest_id=-1456928&dest_type=city&checkin_year=&checkin_month=&checkout_year=&checkout_month=&group_adults=2&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1"

response = requests.get(url,headers=headers)

soup = BeautifulSoup(response.content,"lxml")


a = soup.select(".fcab3ed991.a23c043802")



pprint(a)