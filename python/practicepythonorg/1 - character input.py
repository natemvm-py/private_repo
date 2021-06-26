#Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input('name: ')
age = int(input('age: '))

agediff = 100 - age
currentyear = 2020

print('hi', name + '. you will turn 100 in the year:', currentyear + agediff)
