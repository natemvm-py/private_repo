#TEST

#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#Remember the rules:
#Rock beats scissors
#Scissors beats paper
#Paper beats rock

playerMove1 = input('Player 1 Move?: ')
playerMove2 = input('Player 2 Move?: ')

playerScore1 = 0
playerScore2 = 0

count = int(input('To the best of?: '))

for i in range(count):
    if(playerMove1 == 'rock' and playerMove2 == 'rock'):
        print('Tie')