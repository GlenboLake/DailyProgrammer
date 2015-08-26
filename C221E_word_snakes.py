words = input('Words to snake: ').split()
pos = (0, 0)
index = 0
grid = {}
direction = (-1, 0)
turning_right = True
record = []


def turn(direction, turning_right):
    return turn_right(direction) if turning_right else turn_left(direction)

def turn_right(direction):
    if direction == (0, 1):
        return (1, 0)
    elif direction == (1, 0):
        return (0, -1)
    elif direction == (0, -1):
        return (-1, 0)
    else:
        return (0, 1)


def turn_left(direction):
    return turn_right(turn_right(turn_right(direction)))


def current_player(direction, turning_right):
    return turn_right(direction) if turning_right else turn_left(direction)


def check(word, direction):
    global pos, grid
    return not any([(pos[0] + direction[0] * i, pos[1] + direction[1] * i) in grid for i in range(1, len(word))]) \
        and pos[0] + direction[0] * len(word) >= 0 \
        and pos[1] + direction[1] * len(word) >= 0


while index < len(words):
    if check(words[index], turn(direction, turning_right)):
        direction = turn(direction, turning_right)
    elif check(words[index], turn(direction, not turning_right)):
        turning_right = not turning_right
        direction = turn(direction, turning_right)
    else:
        # Back up a word.
        delete_word, delete_pos, delete_direction = record.pop()
        for i in range(len(delete_word)):
            del grid[(delete_pos[0] + delete_direction[0] * i,
                      delete_pos[1] + delete_direction[1] * i)]
        pos = delete_pos
        direction = turn_right(turn_right(delete_direction))
        index -= 1
        
    # Proceed
    record.append((words[index], pos, direction))
    for i, letter in enumerate(words[index]):
        grid[(pos[0] + direction[0] * i, pos[1] + direction[1] * i)] = letter
    pos = (pos[0] + direction[0] * (len(words[index]) - 1),
           pos[1] + direction[1] * (len(words[index]) - 1))
    index += 1

# Render!
max_rows = max([row for row, col in list(grid.keys())])
for row in range(max_rows + 1):
    row_length = max([c for r, c in list(grid.keys()) if r == row]) + 1
    print(''.join([grid.get((row, col), ' ') for col in range(row_length)]))
