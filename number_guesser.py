import random
random_num = random.randint(0, 10)
print(random_num)
random_num_guess = input('Guess the random number ')

if random_num_guess != int:
    print('Not a number!')
    random_num_guess = input('Guess the random number ')

if int(random_num_guess) > random_num:
    print('Wrong! Number to large.')
    random_num_guess = input('Guess the random number ')

if int(random_num_guess) < random_num:
    print('Wrong! Number to small.')
    random_num_guess = input('Guess the random number ')

if int(random_num_guess) == random_num:
    print('Correct!')

quit()
    
