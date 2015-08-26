class Polynomio(object):

    def __init__(self, cells):
        self.cells = set(cells)
        self.normalize()

    def normalize(self):
        """
        Move as close to (0, 0) as possible with no negative numbers. I may
        or may not have stolen this method from /u/Cosmologicon
        """
        xs, ys = list(zip(*self.cells))
        x0, y0 = min(xs), min(ys)
        self.cells = set((x - x0, y - y0) for x, y in self.cells)

    def _rotate(self, times=1):
        cells = self.cells
        for _ in range(times):
            cells = [(y, -x) for x, y in cells]
        return Polynomio(cells)

    def _flip(self):
        return Polynomio([(-x, y) for x, y in self.cells])

    def variations(self):
        """Rotate and flip to get variation of this polyomino. Useful in seeking uniqueness."""
        polys = []
        for item in range(4):
            p = self._rotate(item)
            polys.append(p)
            polys.append(p._flip())
        return polys

    def grow(self):
        """Find all n+1-ominos that include this shape."""
        adj = set()
        # Get the list of adjacent cells
        for cell in self.cells:
            adj.add((cell[0] - 1, cell[1]))
            adj.add((cell[0] + 1, cell[1]))
            adj.add((cell[0], cell[1] - 1))
            adj.add((cell[0], cell[1] + 1))
        adj = adj - self.cells
        # Make a new polyomino for each adjacent cell and return the unique
        # ones
        new_polys = set()
        for new in adj:
            cells = set(self.cells)
            cells.add(new)
            new_polys.add(Polynomio(cells))
        return new_polys

    def __str__(self):
        xs, ys = list(zip(*self.cells))
        s = []
        for y in range(max(ys) + 1):
            row = [
                '#' if (x, y) in self.cells else ' ' for x in range(max(xs) + 1)]
            s.append(''.join(row).rstrip())
        return '\n'.join(s)

    def __repr__(self, *args, **kwargs):
        return '<Polynomio> ' + repr(sorted(self.cells))

    def __eq__(self, other):
        # Compare cells to avoid recursion
        variations = [v.cells for v in self.variations()]
        return other.cells in variations

    def __hash__(self):
        # For the purpose of sets, we want all "similar" polyominoes to have
        # the same hash. Get all 8 variations, and choose one of them to use
        # regardless
        variations = [hash(str(sorted(list(v.cells))))
                      for v in self.variations()]
        return min(variations)


def build_polynomios(n):
    if n <= 1:
        return set([Polynomio([(0, 0)])])
    else:
        polys = build_polynomios(n - 1)
        bigger = set()
        for poly in polys:
            next_ = poly.grow()
            bigger = bigger.union(next_)
        return bigger


result = build_polynomios(5)
for poly in result:
    print(poly)
    print()
