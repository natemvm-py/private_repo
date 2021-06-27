#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)
#Remember the rules:
#Rock beats scissors
#Scissors beats paper
#Paper beats rock


while(True):
    playerScore1 = 0
    playerScore2 = 0

    count = int(input('To The Best Of?: '))


    while(count > 0):
        playerMove1 = input('Player 1 Move?: ')
        playerMove2 = input('Player 2 Move?: ')

        #Player1 Rock
        if playerMove1 == 'rock' and playerMove2 == 'rock':
            print('Tie!')
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
        elif playerMove1 == 'rock' and playerMove2 == 'paper':
            print('Player 2 Wins!')
            playerScore2 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        elif playerMove1 == 'rock' and playerMove2 == 'scissors':
            print('Player 1 Wins!')
            playerScore1 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        #Player1 Paper
        elif playerMove1 == 'paper' and playerMove2 == 'rock':
            print('Player 1 Wins!')
            playerScore1 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        elif playerMove1 == 'paper' and playerMove2 == 'paper':
            print('Tie!')
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
        elif playerMove1 == 'paper' and playerMove2 == 'scissors':
            print('Player 2 Wins!')
            playerScore2 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        #Player1 Scissors
        elif playerMove1 == 'scissors' and playerMove2 == 'rock':
            print('Player 2 Wins!')
            playerScore2 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        elif playerMove1 == 'scissors' and playerMove2 == 'paper':
            print('Player 1 Wins!')
            playerScore1 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        elif playerMove1 == 'scissors' and playerMove2 == 'scissors':
            print('Tie!')
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
        #Player2 Paper
        elif playerMove2 == 'paper' and playerMove1 == 'rock':
            print('Player 2 Wins!')
            playerScore2 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        elif playerMove2 == 'paper' and playerMove1 == 'paper':
            print('Tie!')
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
        elif playerMove2 == 'paper' and playerMove1 == 'scissors':
            print('Player 1 Wins!')
            playerScore1 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        #Player2 Rock
        elif playerMove2 == 'rock' and playerMove1 == 'rock':
            print('Tie!')
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
        elif playerMove2 == 'rock' and playerMove1 == 'paper':
            print('Player 1 Wins!')
            playerScore1 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        elif playerMove2 == 'rock' and playerMove1 == 'scissors':
            print('Player 2 Wins!')
            playerScore2 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        #Player2 Scissors
        elif playerMove2 == 'scissors' and playerMove1 == 'rock':
            print('Player 1 Wins!')
            playerScore1 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        elif playerMove2 == 'scissors' and playerMove1 == 'paper':
            print('Player 2 Wins!')
            playerScore2 += 1
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
            count -= 1
        elif playerMove2 == 'scissors' and playerMove1 == 'scissors':
            print('Tie!')
            print('Player 1 Score:', playerScore1)
            print('Player 2 Score:', playerScore2)
        else:
            print('Incorrect Input. / rock - paper - scissors \ are the only accepted inputs.')
    if playerScore1 > playerScore2:
        print('Congratulations Player 1!, You Won!')
    elif playerScore2 > playerScore1:
        print('Congratulations Player 2!, You Won!')
    else:
        print('A Tie!')