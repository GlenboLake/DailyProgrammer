size, *grid = open('input/boxes.txt').read().splitlines()
height, width = map(int, size.split())

# Start the heightmap at -1 because the main outer box will be detected
# and increase the height to 0
heightmap = [[-1] * width for _ in range(height)]

legend = {
    0: '#',
    1: '=',
    2: '-',
    3: '.'}


def detect_box(start_row, start_col):
    if grid[start_row][start_col] != '+':
        return None
    # Detect width
    c = start_col + 1
    try:
        while grid[start_row][c] == '-':
            # Follow the top row of ----
            c += 1
    except IndexError:
        # This will happen if a box goes all the way to the right of the area
        return None
    if c == start_col + 1 or grid[start_row][c] != '+':
        return None
    # Detect height
    r = start_row + 1
    try:
        while grid[r][start_col] == '|' and grid[r][c] == '|':
            # Follow the left and right columns of |
            r += 1
    except IndexError:
        # This will happen if a box goes all the way to the bottom of the area
        return None
    if r == start_row + 1 or grid[r][start_col] != '+' or grid[r][c] != '+':
        # Verify corners
        return None
    if any(ch != '-' for ch in grid[r][start_col + 1:c]):
        # Verify bottom row
        return None
    return(start_row, start_col, r, c)

for r, row in enumerate(grid):
    for c, char in enumerate(row):
        if char == '+':
            # See if this is the top-left of a box
            box = detect_box(r, c)
            if box:
                # If so, increase the heightmap for its area.
                for x in range(box[0], box[2]):
                    for y in range(box[1], box[3]):
                        heightmap[x][y] += 1
# Output the result
for r in range(height):
    s = ''
    for c in range(width):
        s += grid[r][c].strip() or legend.get(heightmap[r][c], ' ')
    print(s)
