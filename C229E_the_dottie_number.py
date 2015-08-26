import math


def dottie(func, start):
    current = start
    prev = start + 1
    max_iter = 100000
    while abs(current - prev) > 1e-10 and max_iter:
        max_iter -= 1
        prev = current
        current = func(current)
    if max_iter == 0:
        return None
    return current

print(dottie(math.cos, 0)) # Converges to 0.74
print(dottie(lambda x: x - math.tan(x), 2)) # Converges to pi
print(dottie(lambda x: 1 + 1 / x, 1)) # Converges to phi

logistic = lambda x: 4*x*(1-x)

points = 100
for i in range(points+1):
    result = dottie(logistic, i/points)
    if result is not None:
        print(i/points, result)