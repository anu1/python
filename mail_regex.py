import re
def isValidEmail(email):
	if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email) != None:
		return 1
	return 0	
if isValidEmail("my.email@gmail.com")	== "True":
	print("valid")
else:
	print("not")
		
