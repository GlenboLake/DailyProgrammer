import sys
size, *field = open(sys.argv[1]).read().splitlines()
h,w = list(map(int, size.split()))

def count_neighbors(x, y):
    global field, h, w
    if field[x][y] == ' ':
        return 0
    neighbors = 0
    for dx,dy in [(0,1), (1,0), (0,-1), (-1,0)]:
        if x+dx < 0 or x+dx >= h or y+dy < 0 or y+dy >= w:
            continue
        if field[x+dx][y+dy] != ' ':
            neighbors += 1
    return neighbors

chains = 1
for x in range(h):
    for y in range(w):
        n = count_neighbors(x, y)
        if n > 2:
            chains += n-2
print(chains)