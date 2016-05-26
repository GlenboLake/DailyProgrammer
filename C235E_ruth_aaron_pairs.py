def prime_factor_sum(n):
    i = 2
    factors = set()
    while n > 1:
        while n % i == 0:
            n //= i
            factors.add(i)
        i += 1
    return sum(factors)

with open('input/ruth-aaron.txt') as f:
    for _ in range(int(f.readline())):
        x,y = eval(f.readline())
        print((x,y), 'VALID' if prime_factor_sum(x)==prime_factor_sum(y) else 'NOT VALID')