from math import sqrt

fractions = []
for line in open('input/fractions.txt').read().splitlines():
    fractions.append(list(map(int, line.split('/'))))

def add_fractions(a, b):
    total = (a[0] * b[1] + b[0] * a[1], a[1] * b[1])
    # Reduce
    factor = 2
    while factor <= sqrt(total[1]):
        if total[0] % factor == total[1] % factor == 0:
            total = [x / factor for x in total]
            factor = 2
        else:
            factor += 1
    return tuple(map(int, total))

total = (0, 1)
for fraction in fractions:
    total = add_fractions(total, fraction)
print('{}/{}'.format(*total))
