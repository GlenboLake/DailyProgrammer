from math import sqrt


def solve(number):
    check = int(sqrt(number))
    while number % check != 0:
        check += 1
    return check + (number // check)


if __name__ == '__main__':
    print(solve(12))
    print(solve(456))
    print(solve(4567))
    print(solve(12345))
    print(solve(1234567891011))