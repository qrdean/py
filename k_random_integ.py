#Quinton dean
#This program prints the average of random integers using "random"

import random
number = int(0)
k = eval(input("Give me the number of integers you wish to create "))
for i in range(1,k):
    randomNum = random.randint(1, 999)
    number = randomNum + number
average = float(number/k)
print(format(average, '.2f'))
