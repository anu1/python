import os 
import csv 
import random 
import string
def get_file_path(filename):
	currentdirpath = os.getcwd()
	file_path = os.path.join(os.getcwd(),filename)
	print(file_path)
	return file_path

path = get_file_path('SampleCSVFile_11kb.csv')	

def read_csv(filepath):
	numbers = []
	names = []
	with open(filepath, 'rU',errors='ignore') as csvfile:
		reader = csv.reader(csvfile,delimiter=',')
		#print(reader)
		for row in reader:
			index = row[0]
			name = row[1]
			numbers.append(index)
			names.append(name)
		print(numbers)	
		print(names)
read_csv(path)



