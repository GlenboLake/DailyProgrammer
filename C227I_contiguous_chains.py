import sys
size, *field = open(sys.argv[1]).read().splitlines()
h,w = list(map(int, size.split()))
chains = []

def build_chain(row, col):
    char = field[row][col]
    chain = {(row, col)}
    new = chain.copy()
    while new:
        last_added = new.copy()
        new.clear()
        for x,y in last_added:
            for dx,dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                x2,y2 = x+dx, y+dy
                if (x2, y2) in chain or x2 not in list(range(h)) or y2 not in list(range(w)):
                    continue
                if field[x2][y2] == char:
                    chain.add((x2, y2))
                    new.add((x2, y2))
    return chain

for row in range(h):
    for col in range(w):
        if field[row][col] != ' ':
            if not any([(row,col) in chain for chain in chains]):
                chains.append(build_chain(row,col))
print((len(chains)))