import re
import os
import csv
from collections import Counter
output = {}
dates = []
with open("./fakehost_logs", "r+") as myfile:
	for log_line in myfile: 
		match = re.search(r'^\w+ \d+ \d+:\d+',log_line)
		dates.append(match.group(0))
	output = dict(Counter(dates))	
with open('./fakehost.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames = ["minute", "no.of messages"], delimiter = ',')
    writer.writeheader()	
output_file = open("./fakehost.csv", "a")
for (dt,count) in output.items():
    output_file.write("%s,%s\n" % (dt,count))
