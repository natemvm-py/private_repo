#Create a program that will play the “cows and bulls” game with the user. The game works like this:

#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. 
#For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. 
#Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout the game and tell the user at the end.

import random

sample = '1234567890'
randomNum = random.sample(sample, 4)

def determine_cow_bull(rand_num, cows, bulls):
	while cows != 4:
		user_num = list(input('Enter Guess: '))
		cows = 0
		bulls = 0
		for i in range(len(rand_num)):
			if rand_num[i] == user_num[i]:
				cows += 1
			elif rand_num[i] in user_num:
				bulls += 1
		print('Cows:', cows)
		print('Bulls:', bulls)

determine_cow_bull(randomNum, 0, 0)
	
print('You Got It!')
print('Game Over')