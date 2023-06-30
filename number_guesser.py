import random

def get_max_min():
    maxmin = []
    while True:
        maximum = input('Choose a maximum number: ')
        if maximum.isdigit() == True:
            break
        else:
            print('Enter a number next time!')
            continue
    while True:
        minimum = input('Choose a minimum number: ')
        if minimum.isdigit() == True:
            break
        else:
            print('Enter a number next time!')
            continue
    if int(minimum) >= int(maximum):
        print('Minimum number cannot be greater than maximum!')
        return None
    else:
        maximum = int(maximum)
        minimum = int(minimum)
        maxmin.append(minimum)
        maxmin.append(maximum)
        return maxmin

maxmin = get_max_min()
while maxmin == None:
    maxmin = get_max_min()

random_num = random.randint(maxmin[0], maxmin[1])

#Guessing random number input

def isGuessCorrect(guess):
    if type(guess) != int:
        return 'not number'
    if guess == random_num:
        return True
    if guess > random_num:
        return 'large'
    if guess < random_num:
        return 'small'
    
def guessIsCorrect():
    print('Correct!')
    if guesses == 1:
        print(f'It took you {guesses} try to guess correctly!')
    else:
        print(f'It took you {guesses} tries to guess correctly!')
    quit()

def guessIsIncorrect(num):
    if isGuessCorrect(num) == 'not number':
        print('That is not a number!')
        number_guesser(input('What is the random number? '))
    elif isGuessCorrect(num) == 'large' or isGuessCorrect(num) == 'small':
        print(f'That number is too {isGuessCorrect(num)}.')
        number_guesser(input('What is the random number? '))
        
guesses = 0 

def number_guesser(num):
    global guesses
    
    guesses += 1
    if num.isdigit() == True:
        num = int(num)
        if isGuessCorrect(num) == True:
            return guessIsCorrect()
        if isGuessCorrect(num) != True:
            return guessIsIncorrect(num)
    else:
        print('You need to enter a number next time!')
        guessIsIncorrect(num)

number_guesser(input('What is the random number? '))