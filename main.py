import random
import sys

print('wellcome to the text version of snakes and ladders press Enter to roll the dice or type exit(to leave)')
print('rules are simple 5 snakes that swallow you and 5 ladders to help you climb try and reach 100')

player_position = 0
roll_dice = None

while roll_dice !='exit':
    dice = random.randint(1, 6)
    roll_dice = input(': ')
    print(f"dice rolled to {dice}")
    if roll_dice == '':
        player_position += dice
        print(f"you are at number {player_position} on the board")
    #ladders
    if player_position == 4:
        player_position += 15
        print(f"you reached a ladder so you are at number {player_position} on the board")

    elif player_position == 22:
        player_position += 10
        print(f"you reached a ladder so you are at number {player_position} on the board")

    elif player_position == 40:
        player_position += 12
        print(f"you reached a ladder so you are at number {player_position} on the board")

    elif player_position == 56:
        player_position +=20
        print(f"you reached a ladder so you are at number {player_position} on the board")

    elif player_position == 82:
        player_position += 8
        print(f"you reached a ladder so you are at number {player_position} on the board")

    #snakes

    if player_position ==16:
        player_position -= 12
        print(f"you got swallowed up by a snake so you are at number {player_position} on the board")

    elif player_position == 30:
        player_position -= 8
        print(f"you got swallowed up by a snake so you are at number {player_position} on the board")

    elif player_position == 53:
        player_position -= 30
        print(f"you got swallowed up by a snake so you are at number {player_position} on the board")

    elif player_position == 87:
        player_position -= 85
        print(f"you got swallowed up by a snake so you are at number {player_position} on the board")

    elif player_position == 99:
        player_position -= 46
        print(f"you got swallowed up by a snake so you are at number {player_position} on the board")

    if player_position > 100:
        player_position -= 15
        print(f"-15 you are at number {player_position} on the board")

    if player_position == 100:
            print('WELL-DONE!!\nyou reached 100!')
            sys.exit()
