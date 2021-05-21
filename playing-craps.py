#Program Name: playing-craps.py
#Assignment Module 3
#Class 44680 Block 44599 Section 01
#Michael Baumli
#Date: 20210519


#Copied from the Book and probably butchered for my needs
import random

def roll_dice():
    die1 = random.randrange(1,7)
    die2 = random.randrange(1,7)
    return(die1,die2)

def display_dice(dice):
    die1,die2 = dice
    '''
    print(f'Player rolled {die1} + {die2} = {sum(dice)}')
    '''

def play_craps():
    die_values = roll_dice()
    display_dice(die_values)

    # determine game status and point based on first roll
    sum_of_dice = sum(die_values)


    if sum_of_dice in (7,11): #Winning
        game_status = "WON"
    elif sum_of_dice in(2,3,12): #Losing
        game_status = "LOST"
    else: #Remember point?
        game_status = "CONTINUE"
        my_point = sum_of_dice
        '''
        print('Point is',my_point)
        '''
    while game_status == 'CONTINUE':
        die_values = roll_dice()
        display_dice(die_values)
        sum_of_dice = sum(die_values)

        if sum_of_dice == my_point:
            game_status = 'WON'
        elif sum_of_dice == 7:
            game_status = 'LOST'

    if game_status == 'WON':
        '''
        print('Player wins')
        '''
    else:
        '''
        print('Player loses')
        '''
    return game_status

wins = 0
loses = 0
faces = [0,0,0,0,0,0,0,0,0,0,0,0]

for x in range(6):

    game = play_craps()
    if game == 'WON':
        wins +=1
    else:
        loses +=1

#print(f'You won {wins} times')
#print(f'You lost {loses} times')

for x in range(6000000):
    die_values = roll_dice()
    display_dice(die_values)
    sum_of_dice = sum(die_values)
    faces[sum_of_dice-1]+=1
print("Face                 Frequency")
for x in range(12):
    x1 = x+1
    print(str(x1).rjust(4),end=' ')
    print(str(faces[x]).rjust(25))
print(f"Craps: {(faces[1]+faces[2]+faces[11])/6000000}")
print(f"Win: {(faces[6]+faces[10])/6000000}")

