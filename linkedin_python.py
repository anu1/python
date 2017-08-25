
import oauth2 as oauth
from linkedin import linkedin

import socket
origGetAddrInfo = socket.getaddrinfo

def getAddrInfoWrapper(host, port, family=0, socktype=0, proto=0, flags=0):
    return origGetAddrInfo(host, port, socket.AF_INET, socktype, proto, flags)

    # replace the original socket.getaddrinfo by our version
socket.getaddrinfo = getAddrInfoWrapper

API_KEY = '81ufotojsbr7p6'
API_SECRET = '2pMIJAu4LeOXwFjS'

RETURN_URL = 'https://localhost/auth/linkedin/callback'

authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, RETURN_URL, linkedin.PERMISSIONS.enums.values())
print(authentication.authorization_url)  # open this url on your browser
application = linkedin.LinkedInApplication(authentication)

code=input("Enter Auth Code here: ")
print("Entered code = " + code);
authentication.authorization_code = code
application = linkedin.LinkedInApplication(token=authentication.get_access_token())

profile = application.get_profile()
print(profile);

#application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'num-connections', 'skills', 'educations'])


