import itertools
from datetime import datetime


def sets_of_size(items, count):
    return itertools.combinations(items, count)

start = datetime.now()

lines = open('input/cave of prosperity.txt').readlines()
capacity = float(lines[0])
nuggets = list(map(float, lines[2:2 + int(lines[1])]))

best = tuple()
for size in reversed(list(range(len(nuggets)))):
    print(size)
    biggest = 0
    for subset in sets_of_size(nuggets, size):
        subset_sum = sum(subset)
        if subset_sum > biggest:
            biggest = subset_sum
        if subset_sum > sum(best) and subset_sum <= capacity:
            best = subset
    if biggest < sum(best):
        break

end = datetime.now()
print(sum(best))
for gold in best:
    print(gold)
print(end - start)