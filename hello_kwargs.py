def hello(**kwargs):
	if kwargs is not None:
		for key,value in kwargs.iteritems():
			print("%s == %s" %(key,value))
hello(name="Anu")			
