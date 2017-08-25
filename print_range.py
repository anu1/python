import random
my_list=random.sample(range(1, 3000), 1000)
print(my_list)
if 1500 in my_list:
	print("Number exists at Index",my_list.index(1500))
