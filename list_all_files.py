import os

list = os.listdir("/home/anu") # dir is your directory path
number_files = len(list)
print(number_files)
for i in list:
	print(i)
