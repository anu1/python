import re

print("enter n value:")
n=int(input())

email = []
print("Enter email-ids:")
for i in range(n):
	i = input()
	email.append(i)
for i in email:
#	print(i)
	result = re.search(r"^[a-z]{1,6}\_{0,1}[0-9]{0,4}@[a-z]{6,}\.[a-z]{2,4}$", i)	
#	print("Result:",result)
	if result:
		print("True",result.group())
	else:
		print("False",result.group())
