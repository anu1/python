import re
#from collections import defaultdict as dd
output = {}
#Parse out the timedate stamp Jan 20 05:22:37 to capture two groups 1.) Jan 20 05:22 2.) log output e.g.  
#R: cs3:  The cool service on fakehost does not appear to be communicating with the cool
regex = re.compile(r'^\w+ \d+ \d+:\d+')
with open("./fakehost_logs", "r+") as myfile:
for log_line in myfile: 
#print("logline = ", log_line)
match = regex.match(log_line)
if match:
if match.group(0):
try:
output[match.group(0)] += 1
except Exception as e: 
output[match.group(0)] = 0
else:
print("Parsing line partically succeeded: %s " % (log_line) )
else:
print("ERROR: Malformed logline %s" % (log_line))
output_file = open("./fakehost.csv", "w+")
for (dt,count) in output.items():
output_file.write("%s,%s\n" % (dt,count))
print()    
