from itertools import combinations
from operator import itemgetter
import time


with open('input/grandmashouse_large.txt') as f:
    _ = f.readline()
    points = sorted([tuple(map(float, line[1:-1].split(', ')))
                     for line in f.read().splitlines()], key=itemgetter(0))


def squared_distance(a, b):
    return (a[0] - b[0])**2 + (a[1] - b[1])**2


def brute_force(points):
    best = None, None
    best_dist = float('inf')
    for a, b in combinations(points, 2):
        dist = squared_distance(a, b)
        if dist < best_dist:
            best_dist = dist
            best = a, b
    return best, best_dist


def split(points):
    if len(points) <= 3:
        return brute_force(points)
    middle = len(points) // 2

    left_pair = split(points[:middle])
    right_pair = split(points[middle:])
    min_distance = min([left_pair, right_pair], key=itemgetter(1))

    candidates = [p for p in points if squared_distance(
        p, points[middle]) < min_distance[1]]
    if len(candidates) > 1:
        best_candidates = brute_force(candidates)
        return min([best_candidates, min_distance], key=itemgetter(1))
    return min_distance

start = time.clock()
answer = split(points)[0]
t = time.clock() - start
print('Splitting:', *answer)
print(t, 'seconds')
start = time.clock()
answer = brute_force(points)[0]
t = time.clock() - start
print('Brute force:', *answer)
print(t, 'seconds')
