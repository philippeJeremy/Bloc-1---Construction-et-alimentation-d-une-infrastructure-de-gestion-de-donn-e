import requests
import json



villes = ["Mont Saint Michel","St Malo","Bayeux","Le Havre","Rouen","Paris","Amiens","Lille","Strasbourg","Chateau du Haut Koenigsbourg","Colmar","Eguisheim","Besancon","Dijon","Annecy","Grenoble","Lyon","Gorges du Verdon","Bormes les Mimosas","Cassis","Marseille","Aix en Provence","Avignon","Uzes","Nimes","Aigues Mortes","Saintes Maries de la mer","Collioure","Carcassonne","Ariege","Toulouse","Montauban","Biarritz","Bayonne","La Rochelle"]

position = {}
for ville in villes:
    url = f"https://nominatim.openstreetmap.org/?addressdetails=1&q={ville}&format=json&limit=1"
    r = requests.get(url)
    lat = r.json()[0]["lat"]
    lon = r.json()[0]["lon"]
    position =  {ville : {"latitude" : lat ,"longitude":lon}}
    with open('position.json', 'a') as f:
        json.dump(position, f)
        f.write("\n")









