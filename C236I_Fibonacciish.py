def fib(start, max_value):
    if max_value < start:
        return [0]
    seq = [0, start]
    while seq[-1] < max_value:
        seq.append(seq[-1] + seq[-2])
    return seq

def find_seq(value):
    base = fib(1, value)
    if value in base:
        return base
    for i in reversed(base):
        if value % i == 0:
            break
    return fib(value // i, value)

print(*find_seq(21))
print(*find_seq(84))
print(*find_seq(0))
print(*find_seq(578))
print(*find_seq(123456789))
