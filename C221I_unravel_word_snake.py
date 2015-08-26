grid = open('input/snake.txt').read().splitlines()

pos = [0, 0]
word = grid[0][0]
words = []
direction = [0, 1] if grid[1][0] == ' ' else (1, 0)

def get(pos, direction):
    x = pos[0] + direction[0]
    y = pos[1] + direction[1]
    if x < 0 or y < 0:
        return ' '
    try:
        return grid[x][y]
    except IndexError:
        return ' '

while True:
    while get(pos, direction) != ' ':
        pos = [a+b for a,b in zip(pos, direction)]
        word += grid[pos[0]][pos[1]]
    words.append(word)
    word = word[-1]
    direction = direction[::-1]
    if get(pos, direction) == ' ':
        direction = [-direction[0], -direction[1]]
    if get(pos, direction) == ' ':
        break
print(' '.join(words))