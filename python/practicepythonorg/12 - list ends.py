#Write a program that takes a list of numbers 
#(for example, a = [5, 10, 15, 20, 25]) 
#and makes a new list of only the first and last elements of the given list. 
#For practice, write this code inside a function

import random

list = []
newList = []

#Creating a random list
for i in range(10):
	list.append(random.randint(1,99))

print(list)

#Function that finds first and last element
def first_last(list):
	newList.append(list[0]) #Appends first element to new list
	newList.append(list[-1]) #Appends last element to new list.

first_last(list) #Executing function

print(newList) #Printing results
	