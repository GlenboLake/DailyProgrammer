
def print_rotated_maze(maze):
    # Assume that all cells intersections do have a +.
    cell_size = maze[0].find('+', 1)
    # Get the maze size, then get the "true" size. E.g.:
    # "+--+--+--+" doesn't get printed count as a row
    # "|  |     |" does. Likewise for columns.
    h = len(maze)
    h = int(h - (h + cell_size - 1) / cell_size)
    w = max(list(map(len, maze)))
    w = int(w - (w + cell_size - 1) / cell_size)
    canvas = [[' '] * (h + w) for _ in range(h + w)]
    for r, row in enumerate(maze):
        for c, char in enumerate(row):
            if char == '-':
                # Get the actual row/column if we don't include the ones
                # discounted in the calculation of h and w
                true_row = int(r - r / cell_size)
                true_column = int(c - c / cell_size - 1)
                canvas[
                    true_row + true_column][true_column - true_row + h] = '\\'
            elif char == '|':
                true_row = int(r - r / cell_size - 1)
                true_column = int(c - c / cell_size)
                canvas[
                    true_row + true_column][true_column - true_row + h - 1] = '/'
    print('\n'.join([''.join(x) for x in canvas]))


for mazefile in [1,2,3]:
    maze = open('input/maze{}.txt'.format(mazefile)).read().splitlines()[1:]
    print_rotated_maze(maze)
