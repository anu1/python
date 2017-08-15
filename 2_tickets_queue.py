import sys
import deque
class showtickets:
def wait_queue(tickets,pos):
	q = deque()
	counter = 0
	for j in list(tickets):
		print("j : ", j, " -> ", counter == pos , "position : ", pos)
		item = [j, counter==pos]
		print(item)
		q.append(item)
		counter += 1
	print("Queue is : ")
	print(q)

	seconds = 0
	while True:
		item = q.popleft()
		print(item)
		item[0] -= 1
		seconds += 1
		if(item[0] == 0):
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
    	seconds = tick.wait_queue(tickets,pos)
        print ("Total seconds for ", pos, "is ", seconds)

if __name__ == "__main__":
	main()
