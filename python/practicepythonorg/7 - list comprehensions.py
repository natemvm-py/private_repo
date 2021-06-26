#Let’s say I give you a list saved in a variable: 
#a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
#Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.

import random
import time

a = []

#Randomly Generated List
for i in range(10):
    a.append(random.randint(1,100))

print(a)
time.sleep(0.5)
print('Finding All Even Numbers')
time.sleep(0.5)
b = []

for element in a:
    if element % 2 == 0:
        b.append(element)

print(b)