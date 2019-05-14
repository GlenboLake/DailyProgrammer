from collections import defaultdict
from copy import deepcopy
from functools import reduce
from itertools import combinations


def gen_squares(max_val):
    for i in range(1, max_val):
        if i * i > max_val:
            break
        yield i * i


def get_pairs(n):
    squares = list(gen_squares(2 * n + 1))
    rv = defaultdict(list)
    for a, b in combinations(range(1, n + 1), 2):
        if a + b in squares:
            rv[a].append(b)
            rv[b].append(a)
    return rv


def construct_basic_chains(pairs):
    simple = {k: v for k, v in pairs.items() if len(v) == 2}
    islands = [k for k, v in pairs.items() if len(v) == 1]
    chains = []
    for i in islands:
        if pairs[pairs[i][0]][0] == i:
            chain = [i, pairs[i][0]]
            if chain[::-1] not in chains:
                chains.append(chain)

    while simple:
        value = min(simple)
        neighbors = simple.pop(value)
        chain = [neighbors[0], value, neighbors[1]]
        while chain[0] in simple:
            a, b = simple.pop(chain[0])
            if a == chain[1]:
                chain.insert(0, b)
            else:
                chain.insert(0, a)
        while chain[-1] in simple:
            a, b = simple.pop(chain[-1])
            if a == chain[-2]:
                chain.append(b)
            else:
                chain.append(a)
        chains.append(chain)
    return chains


def solve(n):
    pairs = get_pairs(n)
    ends = [k for k, v in pairs.items() if len(v) == 1]
    if len(ends) > 2:
        return 'Not possible'
    chains = construct_basic_chains(pairs)
    while len(chains) > 1:
        loose_ends = sorted([c[0] for c in chains] + [c[-1] for c in chains if len(c) > 1])
        connections = {end for end in loose_ends if loose_ends.count(end) == 2}
        for conn in connections:
            a, b = [c for c in chains if conn in (c[0], c[-1])]
            chains.remove(a)
            chains.remove(b)
            if a[0] == conn:
                a = a[::-1]
            if b[-1] == conn:
                b = b[::-1]
            chains.append(a + b[1:])
        used = reduce(lambda a, b: a | b, map(set, [c[1:-1] for c in chains]))
        remaining = {k: [n for n in v if n not in used] for k, v in pairs.items() if k not in used}
        remaining = {k: v for k, v in remaining.items() if v}
        chains.extend(construct_basic_chains(remaining))
    return chains[0]


if __name__ == '__main__':
    print(solve(15))
    print(solve(8))
    print(solve(23))
