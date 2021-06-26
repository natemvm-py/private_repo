#Take a list, say for example this one:
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#and write a program that prints out all the elements of the list that are less than 5.

#Extras:
#Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
#Write this in one line of Python.
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

import time

list = [1, 2, 3, 3, 5, 6, 6, 11, 14, 21, 47, 55, 63, 67]

print(list)

num = int(input('Number: '))

list5 = []

time.sleep(0.2)
print('Organizing . ')
time.sleep(0.35)
print('Organizing . . ')
time.sleep(0.5)
print('Organizing . . . ')
time.sleep(0.65)

for x in list:
    if x <= num:
        list5.append(x)

print(list5)

#One-line extra
print([a for a in list if a <= num])