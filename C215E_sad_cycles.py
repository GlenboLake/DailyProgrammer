import sys
def sad_cycle(b,n):
    cycle = [n]
    while True:
        digits = list(map(int, list(str(n))))
        n = sum([d**b for d in digits])
        if n in cycle:
            idx = cycle.index(n)
            cycle = cycle[idx:]
            break
        cycle.append(n)
    return ', '.join(map(str, cycle))

if __name__ == '__main__':
    base = int(sys.argv[1])
    start = int(sys.argv[2])
    print(sad_cycle(base, start))
    
    # other cases:
    print(sad_cycle(6, 2))
    print(sad_cycle(7, 7))
    print(sad_cycle(3, 14))
    print(sad_cycle(11, 2))