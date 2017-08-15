with open('./11_sample.csv') as data:
	for line in data:
		order = line.replace("\n","; ")
		print(order,end="")
print()		
