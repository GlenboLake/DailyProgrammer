import itertools
from math import floor, sqrt
input_ = open('input/crops.txt').read().splitlines()
h, w, r = list(map(int, input_[0].split()))

crops = []
for x, row in enumerate(input_[1:]):
    for y, spot in enumerate(row):
        if spot == 'x':
            crops.append((x, y))
crops.sort()
max_ = 0
sprinkler = None


def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

for x, y in itertools.product(list(range(h)), list(range(w))):
    count = -1 if (x, y) in crops else 0
    for a, b in crops:
        if floor(dist(x, y, a, b)) <= r:
            count += 1
    if count > max_:
        max_ = count
        sprinkler = (x, y)
print(sprinkler)

watered = {'.': '~', 'x': '$'}
for x, row in enumerate(input_[1:]):
    printed_row = ''
    for y, spot in enumerate(row):
        if (x,y) == sprinkler:
            printed_row += '%'
        elif floor(dist(x, y, *sprinkler)) <= r:
            printed_row += watered[spot]
        else:
            printed_row += spot
    print(printed_row)
