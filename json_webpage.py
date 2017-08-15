import socket
origGetAddrInfo = socket.getaddrinfo

def getAddrInfoWrapper(host, port, family=0, socktype=0, proto=0, flags=0):
    return origGetAddrInfo(host, port, socket.AF_INET, socktype, proto, flags)

        # replace the original socket.getaddrinfo by our version
socket.getaddrinfo = getAddrInfoWrapper

import urllib
import requests
import json
url = "http://maps.googleapis.com/maps/api/geocode/json?address=google"
response = urllib.request.urlopen(url)
data = json.loads(response.read())
print(data['status'])

