from math import gcd


def does_collide(height, width, row, column):
    left = height / width * column
    right = height / width * (column + 1)
#     print('{},{} = {} {}\t{} {}'.format(row, column, left, right, left >= (row), right <= (row+1)))
    return max(left, right) >= row and min(left, right) <= (row + 1)


def count_collisions(height, width):
    return height + width - gcd(height, width)


def draw_collisions(height, width):
    for row in range(height)[::-1]:
        print(''.join(["X" if does_collide(
            height, width, row, column) else '.' for column in range(width)]))


def do_the_thing(height, width):
    print(count_collisions(height, width))
    draw_collisions(height, width)

if __name__ == '__main__':
#     do_the_thing(2, 5)
#     do_the_thing(3, 9)
#     do_the_thing(21, 2)
#     # I'm not copying that render onto reddit.
#     print(count_collisions(168, 189))
#     print(count_collisions(100, 101))
    do_the_thing(123456789, 987654321)