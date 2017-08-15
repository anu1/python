import re
from collections import Counter
set_values = set()
set_dates = set()
values = []
dates = []
output = {}
output2 = {}
#Parse out the timedate stamp Jan 20 05:22:37 to capture two groups 1.) Jan 20 05:22 2.) log output e.g.  
#R: cs3:  The cool service on fakehost does not appear to be communicating with the cool
regex = re.compile(r'^(\w+ \d+ \d+:\d+):\d+ \w+ (\w+.*)\[\S+:.*$')
with open("./fakehost_logs", "r+") as myfile:
    for log_line in myfile: 
        match = regex.match(log_line)
        if match:
		print(match.group(1),match.group(2))		
		values.append(match.group(2))
		set_values.add(match.group(2))
		dates.append(match.group(1))
		set_dates.add(match.group(1))
	output = dict(Counter(dates))
	output2 = dict(Counter(values))
#print(values)
#print(set_values)
#print(dates)
#print(set_dates)
#output_file = open("fakehost.csv", "w")
#for (dt,count) in output.items():
#	print("%s,%s" % (dt,count))
#for(k,v) in output2.items():
#	print("%s,%s" % (k,v))
	

