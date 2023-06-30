import time


def start_adventure_stay_still():
    print('As you stay still the bear stares at you.')
    time.sleep(4)
    print('It starts walking closer and closer.') 
    time.sleep(3)
    print('You see it\'s mouth is drooling as it approaches you.')
    time.sleep(3)
    print('The bear whacks you across the head.')
    time.sleep(3)
    print('You die from blood loss. Game over!')

#Cave adventure
def cave_adventure():
    time.sleep(3)
    print('As you walk thorough the cave you see a lake in the cave.')
    time.sleep(3)
    print('You can walk towards the lake or walk outside of the cave.')
    time.sleep(3)
    answer = input('Type: \'walk to the lake\' or \'walk out the cave\': ')
    print('')
    time.sleep(3)
    if answer.lower() == 'walk out the cave':
        print('You walk outside of the cave and see the same viscious bear outside waiting for you.')
        time.sleep(4)
        print('It\'s seen you and is running towards you.')
        time.sleep(3)
        print('You try to run back in the cave but you are too late.')
        time.sleep(3)
        print('You became bear lunch. The end. Game over!')
    if answer.lower() == 'walk to the lake':
        print('You walk towards the lake.')
        lake_adventure()

def mountain_adventure():
    time.sleep(3)
    print('You look around and see vast mountains all around you!')
    time.sleep(3)
    print('There are two paths. Left and right.')
    answer = input('Type: \'Left\' or \'Right\': ')
    if answer.lower() == 'left':
        time.sleep(3)
        print('As you walk you see the bear. \'Gosh again!\' You think to yourself.')
        time.sleep(3)
        print('You run back in the cave to avoid the persistent beast.')
        cave_adventure()  
    if answer.lower() == 'right':
        time.sleep(3)
        print('You walk along a dirt path along a mountain.')
        time.sleep(3)
        print('You find a golden apple tree so you pick up an apple.')
        time.sleep(3)
        print('You turn around and see the bear running at you.')
        time.sleep(3)
        print('You keep your calm and throw the golden apple at it.')
        time.sleep(3)
        print('The bear catches the golden apple out the air with it\'s mouth and swallows it whole.')
        time.sleep(3)
        print('The bear loses it\'s menacing aura and approaches you gracefully.')
        time.sleep(3)
        print('The bear gets close to you and licks your arm. You laugh and give the bear another golden apple from the tree and you take one for yourself.')
        time.sleep(5)
        print('\'Looks delicious\', you think.')
        time.sleep(3)
        print('The end. You win!')
        quit()




def lake_adventure():
    time.sleep(3)
    print('You look inside the lake and see different sea creatures swimming around.')
    time.sleep(4)
    print('You look behing yourself and see the same bear. It\'s found you!')
    time.sleep(4)
    print('The bear starts chasing you.')
    time.sleep(3)
    print('You have two choices. Swim away in the lake or hide.')
    answer = input('Type: \'Swim away\' or \'hide\': ')
    if answer.lower() == 'swim away':
        time.sleep(3)
        print('You start swimming. You see an exit ahead.')
        time.sleep(3)
        print('You make it out the cave.')
        mountain_adventure()
    if answer.lower() == 'hide':
        time.sleep(3)
        print('You sneak to a corner to hide.')
        time.sleep(3)
        print('You feel safe.')
        time.sleep(3)
        print('You feel water drippng on your head so you look up.')
        time.sleep(3)
        print('There\'s the bear hovering above you.')
        time.sleep(3)
        print('It gobbles you down. The end!')
    else:
        time.sleep(3)
        print('Not a valid move! You look around confused.')
        time.sleep(3)
        print('The bear catches you and gobbles you down! The end!')





name = input('Type your name: ')
print('Welcome', name, 'to this adventure!')

#Starting adventure!
time.sleep(3)
print('You are in a valley with many trees towering over you.')
time.sleep(3)
print('You hear a brushing noise behind you so you turn around.')
time.sleep(3)
print('You see a huge viscious looking bear staring at you with sharp teeth!')
time.sleep(3)
print('You have three options! Run to the cave behind you. Stay still. Or sneak to the mountains to your right.')
time.sleep(4)

next_adventure = input('Type: \'Stay still\' or \'Run to the cave\' or \'Sneak to the mountains\': ')
time.sleep(3)
print('')
#Choices
if next_adventure.lower() == 'stay still':
    start_adventure_stay_still()

elif next_adventure.lower() == 'run to the cave':
    print('You start running to the cave.')
    time.sleep(3)
    print('The bear notices you and starts chasing you.')
    time.sleep(3)
    print('You start running faster.')
    time.sleep(3)
    print('You make it to the cave unharmed. Luckily the cave was close or you would\'ve been bear meat!')
    cave_adventure()

elif next_adventure.lower() == 'sneak to the mountains':
    time.sleep(3)
    print('You start to sneak towards the mountains.')
    time.sleep(3)
    print('The bear does\'t notice you.')
    time.sleep(3)
    print('You make it to the vast mountains.')
    mountain_adventure()

else:
    print('Not a valid option. The bear ran towards you and gobbled you up.')
    time.sleep(3)
    print('You lose!')