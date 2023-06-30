import random

user_wins = 0
cp_wins = 0
options = ['rock', 'paper', 'scissors']


def is_user_round_winner(plyr1, plyr2):
    if plyr1 == 'scissors' and plyr2 == 'paper' or plyr1 == 'paper' and plyr2 == 'rock' or plyr1 == 'rock' and plyr2 == 'scissors':
        return True
    elif plyr1 == plyr2:
        return 'Draw'
    else:
        return False
    

while True:

    if user_wins == 3:
        print(f'You won 3 rounds. You win the game!')
        break

    elif cp_wins == 3:
        print(f'Your opponent won 3 rounds before you. You lose!')
        break

    user_move = input('Type rock, paper, scissors or Q to quit: ')
    if user_move.lower() == 'q':
        break
    if user_move not in options:
        print('Move not valid!')
        continue

    random_number = random.randint(0, 2)
    cp_move = options[random_number]

    user_won_round = is_user_round_winner(user_move, cp_move)

    if user_won_round == True:
        print(f'Opponent played {cp_move}. You won this round!')
        user_wins += 1
        continue

    elif user_won_round == False:
        print(f'Opponent played {cp_move}. You lost this round!')
        cp_wins += 1
        continue

    else:
        print(f'Opponent played {cp_move}. This round is a draw!')
        continue

print('Goodbye!')

    
    


