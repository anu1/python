from os import walk, sep
from os.path import basename, isdir
from sys import argv

def tree(startpath, print_files=False):
  for root, subdirs, files in walk(startpath):
		level = root.replace(startpath, '').count(sep)
		indent = '  |' * (level-1) + '  +- '
		print "%s%s/" % (indent, basename(root))
		#print "{}{}/".format(indent, os.path.basename(root))
		subindent = '  |' * (level) + '  +- '
		if print_files:
			for f in files:
				print "%s%s" % (subindent, f)
				#print "{}{}/".format(subindent, f)

tree("/home/anu/python","True")
