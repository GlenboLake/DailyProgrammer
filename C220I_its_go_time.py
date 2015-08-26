def get_adjacent(row, col, char):
    """Get instances of char adjacent to row,col."""
    adj = set()
    if row > 0 and board[row - 1][col] == char:
        adj.add((row - 1, col))
    if row < h - 1 and board[row + 1][col] == char:
        adj.add((row + 1, col))
    if col > 0 and board[row][col - 1] == char:
        adj.add((row, col - 1))
    if col < w - 1 and board[row][col + 1] == char:
        adj.add((row, col + 1))
    return adj


def get_group(row, col, char=None):
    """Get the group that includes row,col; optionally look for specific character."""
    if row not in list(range(h)) or col not in list(range(w)):
        return set()
    if char:
        if board[row][col] != char:
            return set()
    else:
        char = board[row][col]
    group = set([(row, col)])
    adj = get_adjacent(row, col, char)
    group.update(adj)
    while adj:
        prev_adj = adj
        adj = set()
        for cell in prev_adj:
            adj.update(get_adjacent(cell[0], cell[1], char))
        adj -= group
        group.update(adj)
    return group


def has_liberties(group):
    """Does a group have adjacent liberties?"""
    for cell in group:
        if get_adjacent(cell[0], cell[1], ' '):
            return True
    return False


def test_cell(row, col):
    """Get the number of opponent stones removed for placing in row,col."""
    if board[row][col] != ' ':
        return 0
    board[row][col] = player
    groups = [get_group(row + 1, col, opponent)]
    g = get_group(row - 1, col, opponent)
    if g not in groups:
        groups.append(g)
    g = get_group(row, col + 1, opponent)
    if g not in groups:
        groups.append(g)
    g = get_group(row, col - 1, opponent)
    if g not in groups:
        groups.append(g)
    score = sum([len(group) for group in groups if not has_liberties(group)])
    board[row][col] = ' '
    return score

with open('input/go.txt') as f:
    w, h = list(map(int, f.readline().split()))
    player = f.readline().strip('\n')
    board = [list(line.strip('\n')) for line in f.readlines()]
opponent = 'w' if player == 'b' else 'b'

# print '\n'.join([''.join(row) for row in board])

best, cell = 0, 'No constructive move'
for row in range(h):
    for col in range(w):
        score = test_cell(row, col)
        if score > best:
            best = score
            cell = (col, row)
print(cell)
