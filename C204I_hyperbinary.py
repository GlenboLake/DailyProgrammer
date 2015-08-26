from math import log
from timeit import timeit


def hyperbinary(number, max_place=None):
    if number == 0:
        place = 1 if max_place is None else max_place
        return ['0'*(place+1)]
    place = max_place if max_place is not None else int(log(number, 2))
    if place < 0:
        return []
    elif place == 0:
        return list(map(str, list(range(3))))
    reps = []
    for prefix in range(3):
        remainder = number - 2**place * prefix
        if remainder < 0:
            continue
        remainder_reps = hyperbinary(remainder, place - 1)
        for remainder_rep in remainder_reps:
            rep = '{0}{1}'.format(prefix, remainder_rep)
            if sum([2**i * int(v) for i, v in enumerate(reversed(rep))]) == number:
                reps.append(rep)
    if max_place is None:
        reps = [rep.lstrip('0') for rep in reps]
    return reps


if __name__ == '__main__':
    print(hyperbinary(64))
    print('lambda version:', timeit('from dailyprogrammer.C204I_hyperbinary import hyperbinary;set(int(bin(i)[2:])+int(bin(128-i)[2:]) for i in range(128))'))
    print('my version:    ', timeit('from dailyprogrammer.C204I_hyperbinary import hyperbinary;hyperbinary(128)'))

