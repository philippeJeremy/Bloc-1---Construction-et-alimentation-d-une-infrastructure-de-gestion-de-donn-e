# kayak

Date 01/05/2023 au 07/05/2023

Objectif:

Un .csvfichier dans un bucket S3 contenant des informations enrichies sur la météo et les hôtels pour chaque ville française

Une base de données SQL où nous devrions pouvoir obtenir les mêmes données nettoyées de S3

Deux cartes où vous devriez avoir un Top 5 des destinations et un Top 20 des hôtels de la région. Vous pouvez utiliser plotly ou toute autre bibliothèque pour le faire

######################

Utilisez https://nominatim.org/ pour obtenir les coordonnées gps de toutes les villes (pas d'abonnement requis) Documentation : https://nominatim.org/release-docs/develop/api/Search/

Utilisez https://openweathermap.org/appid (vous devez vous abonner pour obtenir une apikey gratuite) et https://openweathermap.org/api/one-call-api pour obtenir des informations sur la météo des 35 villes et mettre dans un DataFrame

#####################

www.booking.com

nom de l'Hotel,
Url vers sa page booking.com,
Ses coordonnées : latitude et longitude
Note donnée par les utilisateurs du site
Description textuelle de l'hôtel


villes : 

["Mont Saint Michel",
"St Malo",
"Bayeux",
"Le Havre",
"Rouen",
"Paris",
"Amiens",
"Lille",
"Strasbourg",
"Chateau du Haut Koenigsbourg",
"Colmar",
"Eguisheim",
"Besancon",
"Dijon",
"Annecy",
"Grenoble",
"Lyon",
"Gorges du Verdon",
"Bormes les Mimosas",
"Cassis",
"Marseille",
"Aix en Provence",
"Avignon",
"Uzes",
"Nimes",
"Aigues Mortes",
"Saintes Maries de la mer",
"Collioure",
"Carcassonne",
"Ariege",
"Toulouse",
"Montauban",
"Biarritz",
"Bayonne",
"La Rochelle"]