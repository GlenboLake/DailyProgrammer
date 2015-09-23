import random


def print_array(array):
    for row in array:
        print(''.join(row))

_, *blueprint = open('input/ascii_house.txt').read().splitlines()

height = len(blueprint) * 2 + 1
width = max([len(b) for b in blueprint]) * 4 + 1
# Pad blueprint with spaces to make it easier
for i in range(len(blueprint)):
    while len(blueprint[i]) < width // 4:
        blueprint[i] += ' '
blueprint = [' ' + row + ' ' for row in blueprint]

result = [[' '] * width for _ in range(height)]

# Get the basic border
# Ground floor is always solid
for i in range(width):
    result[-1][i] = result[-3][i] = '-'
result[-1][0] = result[-1][-1] = '+'
result[-2][0] = result[-2][-1] = '|'
result[-3][0] = result[-3][-1] = '+'
row = -2
# Build the rest of the border
while True:
    try:
        current = ' '
        for i, ch in enumerate(blueprint[row][1:]):
            if ch == '*':
                for j in range(4):
                    # If there's a *, literally raise the roof
                    result[2 * row - 1][4 * i + j] = '-'
                    result[2 * row + 1][4 * i + j] = ' '
            if ch != current:
                # At edges of floors, put the + and |. If it's also a
                # wall below, change a previous + to a |.
                current = ch
                result[2 * row - 1][4 * i] = '+'
                result[2 * row][4 * i] = '|'
                if blueprint[row][i + 1] == blueprint[row + 1][i + 1] and \
                   blueprint[row][i] == blueprint[row + 1][i]:
                    result[2 * row + 1][4 * i] = '|'
                else:
                    result[2 * row + 1][4 * i] = '+'
    except IndexError:
        # This will happen when we pass the top floor and try to access
        # blueprint[row]
        break
    row -= 1
# Add windows
for i, row in enumerate(blueprint):
    for j, ch in enumerate(row[1:-1]):
        if ch == '*' and random.randint(0, 1):
            result[i * 2 + 1][4 * j + 2] = 'o'
# Add the door
door = random.randint(0, len(blueprint[-1]) - 3)
result[-2][4 * door + 1:4 * door + 4] = list('| |')
# Figure out how many rows need to be prepended to render the roofs.
rows_to_add = 0
for i, row in enumerate(blueprint):
    if i > 0:
        # For each row, get the list of roof asterisks. Don't bother with the top row.
        row = ''.join([ch if blueprint[i - 1][j] == ' ' else ' ' for j, ch in enumerate(row)])
    # With the remaining asterisks, find the widest one. 
    roofs = row.split()
    if not roofs:
        break
    rows = 2 * (max([len(r) for r in roofs]) - i)
    rows_to_add = max(rows, rows_to_add)
result = [[' '] * width for _ in range(rows_to_add)] + result
# Now the complicated part: Roofs.
# Start with the roof list -- base height, and left/right ends
roofs = []
# Get the columns of the blueprint (which is currently stored row-indexed)
heights = [''.join([blueprint[i][j] for i in range(len(blueprint))])
           for j in range(len(blueprint[-1]))][1:-1]
# Get the building height in each column
heights = [h.count('*') for h in heights]
current_height = 0
for col, height in enumerate(heights):
    if height != current_height:
        roofs.append([height, col, col])
        current_height = height
    else:
        roofs[-1][-1] = col
# Each item in roofs now has a length-3 list: stories of this part of the
# building, leftmost cell, and rightmost cell
for roof in roofs:
    height = -2 * (roof[0] + 1)
    left = 4 * roof[1] + 1
    right = 4 * (roof[2] + 1) - 1
    while left != right:
        result[height][left] = '/'
        result[height][right] = '\\'
        height -= 1
        left += 1
        right -= 1
    result[height][left] = 'A'

print_array(result)
