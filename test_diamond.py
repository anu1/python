n = 3
if n > 0:
	for i in range(1,n):
		for space in range(n-i):
			print(" ",end="")
		for j in range((2*i)-1):
			print("*",end="")
		print()	
	for i in range(n,0,-1):
		for space in range(n-i):
			print(" ",end="")
		for j in range((2*i)-1):
			print("*",end="")
		print()	
