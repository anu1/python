import json
from pprint import pprint


data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}

json_str = json.dumps(data)
data = json.loads(json_str)
pprint(data)
