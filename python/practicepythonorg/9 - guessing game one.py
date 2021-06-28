#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

#Extras:
#Keep the game going until the user types “exit”. Nate ~ ALSO MADE IT GENERATE NEW RANDOM NUMBER OVER AND OVER UNTIL THE USER TYPES 'exit'.
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random
import time

guessCount = 0
userGuess = 0

num = random.randint(1,100)

print('Welcome To The Guessing Game')
time.sleep(1)
print('Guess A Number From 1 - 100')
time.sleep(1)
print('Type exit To Exit The Game!')
time.sleep(1)
print('Generating Random Number . . . ')
time.sleep(0.5)

while(userGuess != 'exit'):
    userGuess = input('Enter Guess: ')
    if userGuess == 'exit':
        break
    
    userGuess = int(userGuess)
    
    if userGuess > num :
        print('Too High!')
        guessCount += 1
    elif userGuess < num:
        print('Too Low!')
        guessCount += 1
    else:
        print('You Got It!')
        guessCount += 1
        print('You Guessed', guessCount, 'times!')
        time.sleep(0.5)
        print('Game Restarting . . . ')
        time.sleep(0.5)
        print('Generating New Random Number . . . ')
        time.sleep(0.5)
        guessCount = 0
        num = random.randint(1,100)
        continue

print('Game Exit.')