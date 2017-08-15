import  requests
from collections import Counter

url = "http://data.police.uk/api/crimes-street/all-crime?lat=53.396246&lng=-2.646960&date=2013-03"
json_obj = requests.get(url).json()

c = Counter(player['category'] for player in json_obj)
print(c)
