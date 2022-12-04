import os
import json
import requests

from dotenv import load_dotenv

load_dotenv()


villes = ["Le Mont-Saint-Michel","Saint-Malo","Bayeux","Le Havre","Rouen","Paris","Amiens","Lille","Strasbourg","Château du Haut-Kœnigsbourg","Colmar","Eguisheim","Besançon","Dijon","Annecy","Grenoble","Lyon","Gorges du Verdon","Bormes-les-Mimosas","Cassis","Marseille","Aix-en-Provence","Avignon","Uzès","Nîmes","Aigues-Mortes","Les Saintes-Maries-de-la-Mer","Collioure","Carcassonne","Ariège","Toulouse","Montauban","Biarritz","Bayonne","La Rochelle"]
key = os.getenv("APIKEY")

temps = []
for ville in villes:
    url = f"https://nominatim.openstreetmap.org/?addressdetails=1&q={ville}&format=json&limit=1"
    r = requests.get(url)
    lat = r.json()[0]["lat"]
    lon = r.json()[0]["lon"]
    a = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={key}&units=metric")
    data = a.json()
    temps.append({"ville_rechercher" : ville, data.get('list')[1].get('dt_txt'): {"temperature" : data.get('list')[1].get('main').get('temp_max'),
                                                                           "temps" : data.get('list')[1].get('weather')[0].get('description')},
                                        data.get('list')[9].get('dt_txt'): {"temperature" :data.get('list')[9].get('main').get('temp_max'),
                                                                            "temps" : data.get('list')[9].get('weather')[0].get('description')},
                                        data.get('list')[17].get('dt_txt'): {"temperature" :data.get('list')[17].get('main').get('temp_max'),
                                                                            "temps" : data.get('list')[17].get('weather')[0].get('description')},
                                        data.get('list')[25].get('dt_txt'): {"temperature" :data.get('list')[25].get('main').get('temp_max'),
                                                                           "temps" : data.get('list')[25].get('weather')[0].get('description')},
                                        data.get('list')[33].get('dt_txt'): {"temperature" :data.get('list')[33].get('main').get('temp_max'),
                                                                           "temps" : data.get('list')[33].get('weather')[0].get('description')}})
                                 
with open('temps.json', 'w', newline="") as f:
        json.dump(temps, f) 