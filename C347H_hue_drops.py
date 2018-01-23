import copy
from datetime import datetime
from functools import reduce


def parse_input(input_):
    lines = input_.splitlines()
    grid = [line.split() for line in lines[1:-1]]
    return grid, lines[-1]


def get_area(grid):
    cells = set()
    new_cells = {(0, 0)}
    value = grid[0][0]
    while new_cells:
        cells.update(new_cells)
        temp = new_cells.copy()
        new_cells = set()
        for cell in temp:
            adj = [(cell[0] + x, cell[1] + y) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
            adj = [a for a in adj if a[0] >= 0 and a[1] >= 0]
            for r, c in adj:
                try:
                    if grid[r][c] == value:
                        new_cells.add((r, c))
                except IndexError:
                    pass
        new_cells -= cells
    return cells | new_cells


def get_color_options(grid, target):
    colors = set()
    area = get_area(grid)
    for r, c in area:
        adj = [(r + x, c + y) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
        adj = [a for a in adj if a[0] >= 0 and a[1] >= 0]
        for a in adj:
            try:
                colors.add(grid[a[0]][a[1]])
            except IndexError:
                pass
    return (colors - {grid[0][0]}) or {target}


def num_colors_in_grid(grid):
    return len(reduce(lambda a, b: a | b, map(set, grid)))


def solve_any(input_):
    seq = []
    size_seq = []
    grid, target = parse_input(input_)
    while num_colors_in_grid(grid) > 1:
        color = get_color_options(grid, target).pop()
        seq.append(color)
        size_seq.append(len(get_area(grid)))
        for r, c in get_area(grid):
            grid[r][c] = color
    if grid[0][0] != target:
        area = get_area(grid)
        color = target
        seq.append(color)
        for r, c in area:
            grid[r][c] = color
    return ' '.join(seq)


def colors_in_grid(grid):
    return set([color for line in grid for color in line])


def seqs(colors, length, terminal):
    if length == 1:
        yield [terminal]
    else:
        for seq in seqs(colors, length - 1, terminal):
            for color in colors:
                if color != seq[0]:
                    yield [color] + seq


def test_seq(grid, seq):
    grid = copy.deepcopy(grid)
    for color in seq:
        for r, c in get_area(grid):
            grid[r][c] = color
    return num_colors_in_grid(grid) == 1


def solve_short(input_):
    grid, target = parse_input(input_)
    colors = colors_in_grid(grid)
    size = sum(len(line) for line in grid)
    for i in range(len(colors), size + 1):
        print(f'{datetime.now()} testing {i}')
        for seq in seqs(colors, i, target):
            if test_seq(grid, seq):
                return ' '.join(seq)


def flood(grid, colors, start=(0, 0)):
    cells = set()
    new_cells = {start}
    while new_cells:
        cells.update(new_cells)
        temp = new_cells.copy()
        new_cells = set()
        for cell in temp:
            adj = [(cell[0] + x, cell[1] + y) for x, y in [(0, 1), (0, -1), (1, 0), (-1, 0)]]
            adj = [a for a in adj if a[0] >= 0 and a[1] >= 0]
            for r, c in adj:
                try:
                    if grid[r][c] in colors:
                        new_cells.add((r, c))
                except IndexError:
                    pass
        new_cells -= cells
    return cells | new_cells


def regions_of_color(grid, color):
    cells = [(r, c) for r, row in enumerate(grid) for c, cell in enumerate(row) if cell == color]
    return {frozenset(flood(grid, {color}, cell)) for cell in cells}


def solve_greedy(input_):
    grid, target = parse_input(input_)
    target_region_count = len(regions_of_color(grid, target))
    seq = []
    while colors_in_grid(grid) != {target}:
        base = flood(grid, {grid[0][0]})
        colors = colors_in_grid(grid) - {grid[0][0]}
        if target_region_count <= 1:
            colors -= {target}
        if not colors:
            colors = {target}
        scores = {color: flood(grid, {grid[0][0], color}) for color in colors}

        best_choice = max(scores, key=lambda color: len(scores[color]))
        for r, c in base:
            grid[r][c] = best_choice
        seq.append(best_choice)
        target_region_count = len(regions_of_color(grid, target))
    return ' '.join(seq)


if __name__ == '__main__':
    sample = '''4 4 
W O O O 
B G V R
R G B G
V O B R
O'''
    print('Any:', solve_any(sample))
    print('Short:', solve_short(sample))
    print('Greedy:', solve_greedy(sample))
    challenge = '''10 12
W Y O B V G V O Y B
G O O V R V R G O R
V B R R R B R B G Y
B O Y R R G Y V O V
V O B O R G B R G R
B O G Y Y G O V R V
O O G O Y R O V G G
B O O V G Y V B Y G
R B G V O R Y G G G
Y R Y B R O V O B V
O B O B Y O Y V B O
V R R G V V G V V G
V'''
    print(solve_greedy(challenge))
