import sys
from collections import deque
class showtickets:
	def wait_queue(self,tickets,pos):
		q = deque()
		counter = 0
		seconds = 0
		for ntp in list(tickets):  #ntp = no.of tickets per person
			flag = (counter == pos)
			print("No.of tkts per head: ",ntp,"->","Flag: ",flag,"->","position: ",pos)
			item = [ntp,flag] #item is a list
			q.append(item)
			counter += 1
		print("Queue is :  ",q)
		while True:
			item = q.popleft()
			print(item)
			item[0] -= 1 #item[0] is tickets #item[1] is a flag
			seconds += 1
			if(item[0] == 0):
				if(item[1] == True ):
					return seconds
			else:
				q.append(item)
def main():
	tick = showtickets()
	print ("Enter n value :")
	n=int(input())
	tickets=[]
	print("Enter the tickets required :")
	for i in range(n):	
		i = int(input())
		tickets.append(i)
	print ("Enter position: ")
	pos=int(input())
	sec=tick.wait_queue(tickets,pos)
	print ("Total time takem for booking the tickets to the person at position", pos, " is ",sec,"seconds")

if __name__ == "__main__":
	main()
