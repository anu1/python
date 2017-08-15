import re
f=open("logs-python.txt","r")
lines=f.readlines()
result=[]
for x in lines:
	if (re.match(r".*\"(.*\.com)", x)):
		print(re.match(r".*\"(.*\.com)", x ).group(1))
f.close()
