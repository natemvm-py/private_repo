#Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
#(If you don’t know what a divisor is, it is a number that divides evenly into another number. For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

num = int(input('Number: '))
list = range(2,100)
divs = []

for x in list:
    if num % x == 0:
        divs.append(x)

print(divs)