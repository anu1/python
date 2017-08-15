import socket
origGetAddrInfo = socket.getaddrinfo

def getAddrInfoWrapper(host, port, family=0, socktype=0, proto=0, flags=0):
    return origGetAddrInfo(host, port, socket.AF_INET, socktype, proto, flags)

    # replace the original socket.getaddrinfo by our version
socket.getaddrinfo = getAddrInfoWrapper

import urllib.parse
import requests
import re
main_api = 'https://en.wikipedia.org/w/api.php?action=parse&section=0&prop=text&format=json&' 
while True:
	topic = input('Topic: ')

	if topic == 'quit' or topic == 'q':
		break

	url = main_api + urllib.parse.urlencode({'page':topic})
	print(url)

	json_data = requests.get(url).json()
	text2= json_data['parse']['text']['*']
	text1= json_data['parse']['title']
	match2 = re.findall(topic,text2,re.IGNORECASE)
	match1 = re.findall(topic,text1,re.IGNORECASE)
	print("Wikipedia page contains topic ",topic,",",(len(match2)+len(match1)),"times")
