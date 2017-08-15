import os

def list_files(startpath):
	for root, dirs, files in os.walk(startpath):
		print(root,dirs,files)
		level = root.replace(startpath,'').count(os.sep)
		print("****************************")
		print(level,os.path.basename(root))


list_files("/home/anu/python")
