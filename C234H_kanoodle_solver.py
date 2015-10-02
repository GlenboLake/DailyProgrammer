pieces = {
    'A': ((0, 0), (0, 1), (0, 2), (1, 2)),
    'B': ((0, 0), (0, 1), (1, 1), (0, 2), (1, 2)),
    'C': ((0, 0), (0, 1), (0, 2), (0, 3), (1, 3)),
    'D': ((0, 0), (0, 1), (0, 2), (0, 3), (1, 2)),
    'E': ((0, 0), (0, 1), (0, 2), (1, 2), (1, 3)),
    'F': ((0, 0), (0, 1), (1, 1)),
    'G': ((0, 0), (0, 1), (0, 2), (1, 2), (2, 2)),
    'H': ((0, 0), (0, 1), (1, 1), (1, 2), (2, 2)),
    'I': ((0, 0), (0, 1), (1, 1), (2, 1), (2, 0)),
    'J': ((0, 0), (0, 1), (0, 2), (0, 3)),
    'K': ((0, 0), (0, 1), (1, 0), (1, 1)),
    'L': ((0, 1), (1, 0), (1, 1), (1, 2), (2, 1))
}


def rotations(base):
    rot = base
    yield rot
    for _ in range(3):
        rot = tuple((b, -a) for a, b in rot)
        x = min([a for a, _ in rot])
        y = min([b for _, b in rot])
        rot = tuple((a - x, b - y) for a, b in rot)
        yield rot
    rot = tuple((-a, b) for a, b in rot)
    x = min([a for a, _ in rot])
    y = min([b for _, b in rot])
    rot = tuple((a - x, b - y) for a, b in rot)
    yield rot
    for _ in range(3):
        rot = tuple((b, -a) for a, b in rot)
        x = min([a for a, _ in rot])
        y = min([b for _, b in rot])
        rot = tuple((a - x, b - y) for a, b in rot)
        yield rot


def place(piece):
    """All placements of a piece's rotation"""
    xmax, ymax = (5, 3) if piece == pieces['L'] else (11, 5)
    piece_xmax = max([a for a, _ in piece])
    piece_ymax = max([b for _, b in piece])
    dx, dy = xmax - piece_xmax, ymax - piece_ymax
    for x in range(dx):
        for y in range(dy):
            yield tuple((a + x, b + y) for a, b in piece)


# Actually apply the cover problem!
def algorithm_x(matrix, start_column=0, accounted_for=None):
    """Donald Knuth's Algorithm X"""
    if accounted_for is None:
        accounted_for = [0] * len(matrix[0])
    options = [row for row in matrix if row[start_column]]
    for counter, opt in enumerate(options, 1):
        print(start_column, counter)
        ignore = [a or b for a,b in zip(accounted_for, opt)]
        if all(ignore):
            return opt
        cols = [i for i, x in enumerate(opt) if x]
        remains = [row for row in matrix if not any([row[c] for c in cols])]
        if not remains:
            continue
        next_start = start_column + 1
        while not any([row[next_start] for row in remains]):
            next_start += 1
        next_step = algorithm_x(remains, start_column=next_start, accounted_for=ignore)
        if next_step:
            return [opt] + next_step

# Build the matrix: The first 12 columns represent the pieces, and the
# following 55 are the cells in the grid. For each piece, there will be a
# row for each rotation and position, except piece L, which has reflection
# and 90 degree rotation symmetry. This will be limited to one corner.
matrix = []
for piece, base in pieces.items():
    for r in rotations(base):
        for placement in place(r):
            row = [0] * 67
            row[ord(piece) - ord('A')] = 1
            for x, y in placement:
                row[12 + 5 * x + y] = 1
            matrix.append(row)

sample = [
    [1, 0, 0, 0, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 0, 0, 1, 1]]
foo = algorithm_x(sample)

solution = algorithm_x(matrix)
print(solution)