import sys
from collections import deque

class mytickets:

    def calcu(self,tickets,p):
   	 q = deque()
   	 i = 0
   	 for t in list(tickets):
   		 print("t = ", t, " -> ", i == p, " pos = ", p)
   		 item = [t,i==p]
   		 q.append(item)
   		 i += 1
   	 print("dequeue is : ")    
   	 print(q)
   	 # now process the data
    
   	 secs = 0
   	 while True:
   		 item = q.popleft()
   		 print(item)
   		 
   		 #item[0] = tickets needed
   		 # item[1] = position, True or False
   		 
   		 item[0] -= 1 # buy the ticket
   		 secs += 1
   		 if ( item[0] == 0 ):
   			 if ( item[1] == True ): # means it's position
   				 return secs
   		 else:
   				 q.append(item)
   	 # it won't reach here
   	 return 1

def main():
    t1 = mytickets()
    print ("Enter n value :")
    n=int(raw_input())
    tickets=[]
    print ("Enter the tickets required :")
    while (n>0):
   	 ti = int(raw_input())
   	 tickets.append(ti)
   	 n -= 1
    print ("Enter position: ")
    p=int(raw_input())

    # call the calculation function
    secs = t1.calcu(tickets,p)
    print ("Total seconds for ", p, "is ", secs)

if __name__ == "__main__":
    main()

