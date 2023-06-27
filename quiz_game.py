score = 0

print('Welcome to my computer quiz!')
player = input('Do you want to play? ')

if player.lower() != 'yes':
    quit()

print('Ok! Let\'s play.')

#Question 1

print('Question 1:')
q1 = input('What is in the sky and rhymes with fun? ')


if q1.lower() == 'sun':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print('Score: ' + str(score) + '/1')

#Question 2

print('Question 2:')
q2 = input('What walks on four feet during the day, two feet during the evening and three at night? ')


if q2.lower() == 'man':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
print('Score: ' + str(score) + '/2')

#Question 3

print('Last Question:')
q3 = input('What is Obama\'s last name? ')


if q3.lower() == 'obama':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

#End

finalScore = str((score)/3 * 100) + '%'

print('Your final score is ' + finalScore + '.')


if score == 3:
    print('You pass!')
    quit()
else:
    print('Sorry, you failed! You need to get 100% to pass.')
    quit()


