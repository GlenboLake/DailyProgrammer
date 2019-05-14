from random import randint

input_ = '''5d12
6d4
1d2
1d8
3d6
4d20
100d100'''

all_dice = input_.splitlines()


def roll(dice_string):
    count, value = dice_string.split('d')
    total = 0
    for _ in range(int(count)):
        total += randint(1, int(value))
    return total


for _ in range(8):
    print(roll('3d6'))
