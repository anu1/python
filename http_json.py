#https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224


import socket
origGetAddrInfo = socket.getaddrinfo

def getAddrInfoWrapper(host, port, family=0, socktype=0, proto=0, flags=0):
    return origGetAddrInfo(host, port, socket.AF_INET, socktype, proto, flags)

    # replace the original socket.getaddrinfo by our version
socket.getaddrinfo = getAddrInfoWrapper

import urllib.request
import json
import textwrap

with urllib.request.urlopen("https://www.googleapis.com/books/v1/volumes?q=isbn:1101904224") as f:
	text = f.read()
	decodedtext = text.decode('utf-8')
	print(textwrap.fill(decodedtext,width=50))
print()

obj = json.loads(decodedtext)
print(obj['kind'])
print(obj['items'][0]['searchInfo']['textSnippet'])
