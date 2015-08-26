canvas = open('input/Boxes5.txt').read().splitlines()


def scan():
    boxes = 0
    for r, row in enumerate(canvas):
        for c, char in enumerate(row):
            if char != '+':
                continue
            boxes += find_boxes(r, c)
    return boxes


def find_boxes(row, col):
    """Find number of boxes with (row,col) as top left corner"""
    boxes = 0
    possible_widths = find_widths(row, col)
    for width in possible_widths:
        heights = find_heights(row, col, width)
        boxes += len(heights)
    return boxes


def find_widths(row, col):
    """Given a point, find all possible widths of a box.
    
    Essentially the same as searching for instances of regex '\+[-+]+\+'
    """
    widths = []
    for i, char in enumerate(canvas[row][col:]):
        if not i: continue
        if char not in '+-':
            break
        if char == '+':
            widths.append(i)
    return widths

def find_heights(row, col, width):
    """Given a top-left corner and width, find all possible heights for a box."""
    heights = []
    for height in range(1, len(canvas)-row):
        try:
            # Left and right of every row need to be + or | for it to be part of a box.
            if canvas[row+height][col] not in '+|' or \
               canvas[row+height][col+width] not in '+|':
                break
        except IndexError:
            # The next row might not be long enough! Break in that case too.
            break
        if canvas[row+height][col] == canvas[row+height][col+width] == '+':
            # Verify that the bottom of the box is unbroken (i.e., + and - only)
            if set(canvas[row+height][col:col+width]) <= set('+-'):
                heights.append(height)
    return heights

if __name__ == '__main__':
    print('Found {} boxes'.format(scan()))
