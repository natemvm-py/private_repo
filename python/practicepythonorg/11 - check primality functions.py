#Ask the user for a number and determine whether the number is prime or not. 
#(For those who have forgotten, a prime number is a number that has no divisors.). 
#You can (and should!) use your answer to Exercise 4 to help you. 
#Take this opportunity to practice using functions, described below.

num = int(input('Enter Number: '))

if num > 0:
    for i in range(2, num - 1): #This range excludes 'num' variable and 1, both of which 'num' is divisible by.
        if num % i != 0: #If number isnt evenly divisable by i, continue to next i/number.
            continue #If it doesnt equal 0, it coninues through to next i/number
        elif num % i == 0: #Divides evenly, therefore cannot be a prime.
            print('Not A Prime')
            exit()
    print('Is A Prime') #If it comes out of that loop without num % i == 0 it must be a prime.
    
elif num == 0:
    print('Not A Prime')
else:
    print('Not A Prime')