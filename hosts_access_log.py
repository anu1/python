from collections import Counter
filename = "./hosts_access_log_00"
hosts = []
for f in open(filename):
	cols = f.split(' ')
	hosts.append(cols[0])
#print(hosts)
a = dict(Counter(hosts))
f = open("./records_hosts_access_log_00.txt", "w+")
for k,v in a.items():
	f.write("the host {} made {} requests.\n".format(k,v))
f.close()
print()	

