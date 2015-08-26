# Python 3.4!
from math import floor, sqrt, ceil


def gen_spiral(size):
    grid = [None] * size**2
    point = floor(size**2 / 2)
    val = 1
    dist = 1
    d = 0  # direction
    directions = [1, -size, -1, size]
    while not all(grid):
        for _ in range(2):
            for _ in range(dist):
                if val > size**2:
                    break
                grid[point] = val
                val += 1
                point += directions[d]
            d = (d + 1) % len(directions)
        dist += 1
    return grid


def find_number(size, n):
    # Find out which ring this number is on
    ring = ceil(sqrt(n)) // 2
    ring_max = (ring * 2 + 1)**2
    dist_around_ring = ring_max - n
    x = y = ring
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1), (0, 0)]
    d = 0
    while dist_around_ring > ring * 2:
        x += ring * 2 * dirs[d][0]
        y += ring * 2 * dirs[d][1]
        dist_around_ring -= ring * 2
        d += 1
    x += dist_around_ring * dirs[d][0]
    y += dist_around_ring * dirs[d][1]
    return x + 1 + size // 2, y + 1 + size // 2


def number_at(size, x, y):
    # New values based on center being (0, 0)
    x = x - 1 - size // 2
    y = y - 1 - size // 2

    ring = max(list(map(abs, [x, y])))
    ring_max = (2 * ring + 1)**2
    dist_before_turn = 2 * ring
    counter = 0
    dirs = [(-1, 0), (0, -1), (1, 0), (0, 1), (0, 0)]
    d = 0
    at_x, at_y = ring, ring
    value = ring_max
    while (x, y) != (at_x, at_y):
        at_x += dirs[d][0]
        at_y += dirs[d][1]
        value -= 1
        counter += 1
        if counter % dist_before_turn == 0:
            d += 1
    return value


if __name__ == '__main__':
    # Old method
    if False:
        while True:
            try:
                size, *value = list(map(int, input("Query: ").split()))
            except ValueError:
                break
            spiral = gen_spiral(size)
            if len(value) == 0:
                break
            elif len(value) == 1:
                loc = spiral.index(value[0])
                row, col = loc % size + 1, loc // size + 1
                print((row, col))
            elif len(value) == 2:
                x, y = value
                print((spiral[x - 1 + size * (y - 1)]))
            else:
                print("Bad value!")
    else:
        while True:
            try:
                size, *value = list(map(int, input("Query: ").split()))
            except ValueError:
                break
            if len(value) == 0:
                break
            elif len(value) == 1:
                print((find_number(size, value[0])))
            elif len(value) == 2:
                print((number_at(size, *value)))
            else:
                print("Bad value!")
