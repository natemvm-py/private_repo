#This week’s exercise is going to be revisiting an old exercise (see Exercise 5), except require the solution in a different way.
#Take two lists, say for example these two:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). 
#Make sure your program works on two lists of different sizes. Write this using at least one list comprehension. (Hint: Remember list comprehensions from Exercise 7)
#Extra:
#Randomly generate two lists to test this

import random
import time

a = []
b = []
c = []

#Generate two random lists
for i in range(random.randint(5,15)):
	a.append(random.randint(1,99))

for i in range(random.randint(5,15)):
	b.append(random.randint(1,99))

#For Show
print('List 1:', a)
time.sleep(1)
print('List 2:', b)
time.sleep(1)
print('Finding Common Numbers . . . ')
time.sleep(1)

#Finding Common Numbers
for i in a:
	if i in b:
		c.append(i)
		
print('Common Numbers Found:', c)