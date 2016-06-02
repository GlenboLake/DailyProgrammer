import string
import time
import turtle

CELL_SIZE = 16


def xy_from_turtle():
    """Get grid coordinates from turtle location"""
    global CELL_SIZE, t
    return tuple(map(lambda foo: round(foo / CELL_SIZE), t.pos()))


def get_letter():
    """Get the letter at the turtle's location"""
    x, y = xy_from_turtle()
    if x == -1:
        return string.ascii_uppercase[12 - y]
    elif x == 13:
        return string.ascii_lowercase[25 - y]
    elif y == -1:
        return string.ascii_uppercase[13 + x]
    elif y == 13:
        return string.ascii_lowercase[x]


def goto_letter(letter):
    """Jump the turtle to a letter"""
    global CELL_SIZE, t
    t.up()
    if letter in string.ascii_lowercase[:13]:
        x = string.ascii_lowercase.index(letter)
        y = 13
        t.seth(270)
    elif letter in string.ascii_lowercase[13:]:
        x = 13
        y = 25 - string.ascii_lowercase.index(letter)
        t.seth(180)
    elif letter in string.ascii_uppercase[:13]:
        x = -1
        y = 12 - string.ascii_uppercase.index(letter)
        t.seth(0)
    else:  # string.ascii_uppercase[13:]
        x = string.ascii_uppercase.index(letter) - 13
        y = -1
        t.seth(90)
    t.goto(x * CELL_SIZE, y * CELL_SIZE)


def decode_letter(letter):
    """The actual following of the mirrors"""
    global t, grid
    t.hideturtle()
    goto_letter(letter)
    t.showturtle()
    t.forward(CELL_SIZE)
    while get_letter() is None:
        x, y = xy_from_turtle()
        if grid[y][x] == '/':
            if t.heading() in [0,180]:
                t.left(90)
            else:
                t.right(90)
        elif grid[y][x] == '\\':
            if t.heading() in [0,180]:
                t.right(90)
            else:
                t.left(90)
        t.forward(CELL_SIZE)
    return get_letter()

message = 'TpnQSjdmZdpoohd'

# Start setup
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
# Draw the background grid
t.pencolor('lightgray')
turn = 0
t.up()
t.goto(-CELL_SIZE / 2, -CELL_SIZE / 2)
t.down()
for _ in range(2):
    for _ in range(13):
        t.forward(CELL_SIZE * 13)
        t.left(90 + turn)
        t.forward(CELL_SIZE)
        t.left(90 + turn)
        turn = -180 - turn
    turn = 0
    t.forward(CELL_SIZE * 13)
    t.left(90)
# Draw the letters around the border
t.pencolor('black')
t.up()
for i in range(13):
    t.goto(5 - CELL_SIZE - CELL_SIZE / 2, (12 - i) * CELL_SIZE - CELL_SIZE / 2)
    t.write(string.ascii_uppercase[i])
    t.goto(i * CELL_SIZE + 5 - CELL_SIZE / 2, -CELL_SIZE - CELL_SIZE / 2)
    t.write(string.ascii_uppercase[i + 13])
    t.goto(i * CELL_SIZE + 5 - CELL_SIZE / 2, 13 * CELL_SIZE - CELL_SIZE / 2)
    t.write(string.ascii_lowercase[i])
    t.goto(13 * CELL_SIZE + 5 - CELL_SIZE / 2, (12 - i) * CELL_SIZE - CELL_SIZE / 2)
    t.write(string.ascii_lowercase[i + 13])
# Read the mirror array
with open('input/mirror.txt') as f:
    grid = [list(line) for line in f]
grid.reverse()
# Draw the mirrors
for x in range(13):
    for y in range(13):
        mirror = grid[y][x]
        if mirror == '/':
            t.up()
            t.goto((x - .5) * CELL_SIZE, (y - .5) * CELL_SIZE)
            t.down()
            t.goto((x + .5) * CELL_SIZE, (y + .5) * CELL_SIZE)
        elif mirror == '\\':
            t.up()
            t.goto((x + .5) * CELL_SIZE, (y - .5) * CELL_SIZE)
            t.down()
            t.goto((x - .5) * CELL_SIZE, (y + .5) * CELL_SIZE)
t.up()
# Put the encoded message below the grid
t.goto(0, -3 * CELL_SIZE)
t.write(message)
# Offset of where the next decoded letter goes
after = 0, -4 * CELL_SIZE
# Fully decoded message
decoded = ''
t.speed(1)
t.up()
for char in message:
    letter = decode_letter(char)
    time.sleep(0.2)
    t.goto(*after)
    t.seth(0)
    t.write(letter, move=True)
    t.forward(1)  # Kerning.
    after = t.pos()

turtle.mainloop()
