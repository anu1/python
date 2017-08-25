print("Prime numbers between 1 and 10 are:")

for num in range(1,10):
   # prime numbers are greater than 1
   if num > 1:
       for i in range(2,num):
           if (num % i) == 0:
               break
       else:
           print(num)
