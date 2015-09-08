line = [0] + list(map(int, input())) + [0]

for _ in range(25):
    print(''.join(['x' if x else ' ' for x in line[1:-1]]))
    line = [0] + [int(line[i - 1] ^ line[i + 1]) for i, _ in enumerate(line[1:-1], start=1)] + [0]
