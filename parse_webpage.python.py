import socket
origGetAddrInfo = socket.getaddrinfo

def getAddrInfoWrapper(host, port, family=0, socktype=0, proto=0, flags=0):
    return origGetAddrInfo(host, port, socket.AF_INET, socktype, proto, flags)

        # replace the original socket.getaddrinfo by our version
socket.getaddrinfo = getAddrInfoWrapper

import urllib
import requests
import json
#url = 'http://pythonprogramming.net/parse-website-using-regular-expressions-urllib/'
url = 'http://maps.googleapis.com/maps/api/geocode/json?address=524004'
req = urllib.request.urlopen(url)
respData = req.read()
#print(respData)
json_data = json.loads(respData)
print(json_data)
json_status = json_data['status']
if json_status == 'OK':
	print(json_data['results'][0]['address_components'])
