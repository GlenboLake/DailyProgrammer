import sys


class WordGrid(object):
    directions = [(0,1),(1,0),(0,-1),(-1,0)]

    def __init__(self, words):
        # Words to place
        self.wordlist = [w.upper() for w in words]
        # Letters placed in grid, saved as (x,y):letter pairs
        self.placements = {}
        self.total_crossings = 0
        self.solve()

    def place_word(self, word):
        if self.placements:
            xmin = min([p[0] for p in self.placements]) - len(word)
            xmax = max([p[0] for p in self.placements]) + len(word)
            ymin = min([p[1] for p in self.placements]) - len(word)
            ymax = max([p[1] for p in self.placements]) + len(word)
        else:
            xmin = xmax = ymin = ymax = 0
        best_score = -1
        best_placement = None
        for x in range(xmin, xmax+1):
            for y in range(ymin, ymax+1):
                for d in self.directions:
                    score, placement = self.try_place_word(word, x, y, d)
                    if score > best_score:
                        best_score = score
                        best_placement = placement
        if self.placements and not best_score:
            return False
        else:
            self.placements.update(best_placement)
            self.total_crossings += best_score
            return True
        
    def try_place_word(self, word, x, y, direction):
        placement = {}
        for i, letter in enumerate(word):
            px = x + i*direction[0]
            py = y + i*direction[1]
            placement[px,py] = letter
        score = self.validate_placement(placement)
        return score, placement

    def validate_placement(self, placement):
        common_keys = [k for k in placement.keys() if k in self.placements]
        return len(common_keys) if all([placement[k] == self.placements[k] for k in common_keys]) else 0

    def solve(self):
        words = self.wordlist.copy()
        while words:
            word = words.pop()
            if not self.place_word(word):
                words.insert(0, word)

    def render(self):
        grid = []
        # Get offsets
        xoff = min([p[0] for p in self.placements])
        yoff = min([p[1] for p in self.placements])
        for (x, y), letter in self.placements.items():
            try:
                grid[x - xoff][y - yoff] = letter
            except IndexError:
                while len(grid) < x - xoff + 1:
                    grid.append([])
                while len(grid[x - xoff]) < y - yoff + 1:
                    grid[x - xoff].append(' ')
                grid[x - xoff][y - yoff] = letter
        for row in grid:
            print(''.join(row))

words = sys.argv[1].split(',')
grid = WordGrid(words)
grid.render()
print('Crossings:', grid.total_crossings)
