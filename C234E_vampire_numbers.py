from functools import reduce
from itertools import product
from operator import mul
num_digits, num_fangs = map(int, input().split())
fang_size = num_digits // num_fangs

vampires = {}
fang_numbers = range(10**(fang_size-1), 10**fang_size)
for fangs in product(fang_numbers, repeat=num_fangs):
    vampire = reduce(mul, fangs)
    if vampire in vampires:
        continue
    fang_digits = sorted(''.join(map(str, fangs)))
    vampire_digits = sorted(str(vampire))
    if fang_digits == vampire_digits:
        vampires[vampire] = fangs
for v,f in sorted(vampires.items()):
    print('{}={}'.format(v, '*'.join(map(str, f))))