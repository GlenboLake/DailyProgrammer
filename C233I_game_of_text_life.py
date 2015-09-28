import copy
import itertools
import random


class GameOfLife(object):

    def __init__(self, text):
        start = [list(s) for s in text.splitlines()]
        max_width = max([len(s) for s in start])
        for row in start:
            while len(row) < max_width:
                row.append(' ')
        self.grid = start

    def show(self):
        for row in self.grid:
            print(''.join(row))
        print()

    def is_alive(self, row, col):
        return self.grid[row][col] != ' '

    def get_neighbors(self, row, col):
        # Get all combinations of 0/1/-1 except 0,0 (current cell) to check
        # adjacent cells
        adj = [x for x in itertools.product([0, 1, -1], repeat=2) if any(x)]
        n = []
        for dr, dc in adj:
            try:
                if row + dr < 0 or col + dc < 0:
                    raise IndexError
                ch = self.grid[row + dr][col + dc]
                if ch != ' ':
                    n.append(ch)
            except IndexError:
                continue
        return n

    def make_next(self):
        next_gen = copy.deepcopy(self.grid)
        for i, row in enumerate(self.grid):
            for j, _ in enumerate(row):
                neighbors = self.get_neighbors(i, j)
                if self.is_alive(i, j):
                    if len(neighbors) not in [2, 3]:
                        next_gen[i][j] = ' '
                elif len(neighbors) == 3:
                    next_gen[i][j] = random.choice(neighbors)
        self.grid = next_gen

    def play(self, generations=float('inf')):
        gen = 0
        while gen < generations:
            gen += 1
            print(gen)
            self.show()
            self.make_next()

text = open(__file__).read()
GameOfLife(text).play(100)