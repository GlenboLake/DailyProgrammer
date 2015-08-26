def parse(filename):
    lines = [line.strip() for line in open(filename).readlines()]
    return list(map(list, lines[1:-1])), lines[-1].split()


def fill(image, row, col, newchar, oldchar=None):
    try:
        image[col][row]
    except IndexError:
        return image
    if oldchar is None:
        oldchar = image[col][row]
    if image[col][row] == oldchar:
        image[col][row] = newchar
        image = fill(image, row, col + 1, newchar, oldchar)
        image = fill(image, row, col - 1, newchar, oldchar)
        image = fill(image, row - 1, col, newchar, oldchar)
        image = fill(image, row + 1, col, newchar, oldchar)
    return image


def print_image(image):
    print('\n'.join(''.join(row) for row in image))

image, filldata = parse('input/floodfill.txt')
x, y = int(filldata[0]), int(filldata[1])
char = filldata[2]
fill(image, x, y, char)
print_image(image)