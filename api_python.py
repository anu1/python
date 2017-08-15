import requests
from pprint import pprint
response = requests.get("http://samples.openweathermap.org/data/2.5/forecast?id=524901&appid=fb81d4a85192f3e6a305a987d30403e7")
weather = response.json()
#pprint(weather)
#print("The weather for",weather['id'])
print(weather['cod'])
print(weather['list'][0]['dt'])
print(weather['list'][0]['main']['temp'])
#print(weather['list'][0]['weather']['id'])
