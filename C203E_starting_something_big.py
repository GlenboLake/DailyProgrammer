import time
import turtle


t = turtle.Turtle()
t.speed(0)
t.hideturtle()
max_distance = 400
distance = max_distance


def set_color(t):
    r = t.pos()[0] / float(max_distance)
    g = t.pos()[1] / float(max_distance)
    manhattan = sum([abs(foo-max_distance/2) for foo in t.pos()])
    b = 1 - manhattan / max_distance
    t.pencolor((r, g, b))

while distance:
    for i in range(4):
        for _ in range(distance - 1 if i == 3 else distance):
            set_color(t)
            t.forward(1)
        t.left(90)
    set_color(t)
    t.forward(1)
    distance -= 2
t.forward(1)
time.sleep(10)
