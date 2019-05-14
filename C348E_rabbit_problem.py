def solve(males, females, target):
    males = {2: males}
    females = {2: females}
    months = 0
    death_toll = 0
    while sum(males.values()) + sum(females.values()) < target:
        fertile = sum(v for k, v in females.items() if k >= 4)
        death_toll += males.get(96, 0) + females.get(96, 0)
        males = {k + 1: v for k, v in males.items() if k < 96}
        females = {k + 1: v for k, v in females.items() if k < 96}
        males[0] = 5 * fertile
        females[0] = 9 * fertile
        months += 1
    return months, death_toll


print(solve(2, 4, 1000000000))
print(solve(2, 4, 15000000000))
