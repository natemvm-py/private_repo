#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

#Extras:
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

while(True):
    userGuess = -999999
    num = random.randint(1,9)
    print(num)

    if(userGuess != num):
        userGuess = int(input('Enter Guess: '))

        if userGuess == num:
            print('You Got It!')
            continue
        elif userGuess > num :
            print('Too High!')
        elif userGuess < num:
            print('Too Low!')