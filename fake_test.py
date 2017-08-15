import re
import os
import csv
from collections import Counter
output = {}
dates = []
values = []
with open("./fakehost_logs", "r+") as myfile:
	for log_line in myfile: 
		match = re.search(r'^\w+ \d+ \d+:\d+',log_line)
		dates.append(match.group(0))
		list=re.split(' ',log_line)
		list2=re.search(r'\w+',list[4])
		values.append(list2.group(0))
	print(dates)
	print(values)
#	output = dict(Counter(dates))	
#with open('./fakehost.csv', 'w') as csvfile:
#    writer = csv.DictWriter(csvfile, fieldnames = ["minute", "no.of messages","rsyslogd","cs3","ACCT_ADD"], delimiter = ',')
#    writer.writeheader()	
#output_file = open("./fakehost_2.csv", "a")
#for (dt,count) in output.items():
#    output_file.write("%s,%s\n" % (dt,count))
