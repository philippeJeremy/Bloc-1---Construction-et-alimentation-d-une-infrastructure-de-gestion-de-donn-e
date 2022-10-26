from asyncore import write
import requests

key = '9923010e5cc0e36ef98d53d819954dc6'

with open("position.json", "r") as f:
    data = f.read()

# for key, value  in data:
#     print(value)


url = f"https://api.openweathermap.org/data/2.5/onecall?lat=48.6359541&lon=-1.511459954959514&&appid={key}"

r = requests.get(url)
data = r.json()
print(data)