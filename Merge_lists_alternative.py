#! /usr/bin/python

list_a = ["a", "b", "c", "d", "e"]
#list_a = [1, 2, 3, 4]
#list_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_b = [10, 20, 30, 40, 50, 60, 70]
#list_b = [10, 20, 30, 40]
c = 0
tmp_array = []


if len(list_a) > len(list_b):
	for i in range(len(list_b)):
		tmp_array.append(list_a[i])
		tmp_array.append(list_b[i])
	tmp_array.extend(list_a[-c:])
	print("First list:", list_a)
	print("Second list:", list_b)
	print("First list is Bigger in this case")
	print("Final list:", tmp_array)
elif len(list_b) > len(list_a):
	c = (len(list_b) - len(list_a)) 		
	for i in range(len(list_a)):
		tmp_array.append(list_a[i])
		tmp_array.append(list_b[i])
	tmp_array.extend(list_b[-c:])
	print("First list:", list_a)
	print("Second list:", list_b)
	print("Second list is Bigger in this case")
	print("Final list:", tmp_array)
else:
	for i in range(len(list_a)):
		tmp_array.append(list_a[i])
		tmp_array.append(list_b[i])
	print("First list:", list_a)
	print("Second list:", list_b)
	print("Both lists are Equal in this case")
	print("Final list:", tmp_array)
