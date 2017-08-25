double = lambda x: x * 2
print(double(5))
my_list = [1,2,4,6,11,12]
new_list = list(map(lambda x: (x%2 == 0), my_list))
print(new_list)
