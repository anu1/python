import json
from pprint import pprint
with open('log_json.txt') as data_file:
	data = json.load(data_file)
pprint(data)	
pprint(data["om_points"])
pprint(data["maps"][0]["id"])
