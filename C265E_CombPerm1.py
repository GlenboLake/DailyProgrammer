from itertools import combinations, permutations

import math


def format_seq(seq):
    return ' '.join(str(x) for x in seq)


# Itertools
def permutation_itertools(index, count):
    return format_seq(sorted(permutations(range(count)))[index - 1])


def combination_itertools(index, count, total):
    return format_seq(sorted(combinations(range(total), count))[index - 1])


# Reinventing the wheel
def find_permutation(index, count):
    perms = [[x] for x in range(count)]
    for _ in range(count - 1):
        perms = [x + [i] for x in perms for i in range(count) if i not in x]
    return format_seq(perms[index - 1])


def find_combination(index, count, total):
    perms = [[x] for x in range(total)]
    for _ in range(count - 1):
        perms = [x + [i] for x in perms for i in range(x[-1], total) if i not in x]
    result = sorted(perms)[index - 1]
    return format_seq(result)


# Building dynamically
def dynamic_permutations(index, count):
    index -= 1
    digits = list(range(count))
    result = []
    while digits:
        num_perms = math.factorial(len(digits) - 1)
        digit_index = index // num_perms
        result.append(digits.pop(digit_index))
        index -= digit_index * num_perms
    return format_seq(result)


def nCk(n, k):
    if n < k:
        return 1
    from math import factorial as f
    return int(f(n) / (f(k) * f(n - k)))


def dynamic_combinations(index, count, total):
    digits = list(range(total))
    result = []
    for _ in range(count - 1):
        digit_index = 0
        num_of_digit = nCk(len(digits) - digit_index - 1, count - 1)
        combo_index = num_of_digit
        while combo_index < index:
            digit_index += 1
            num_of_digit = nCk(len(digits) - digit_index - 1, count - 1)
            combo_index += num_of_digit
        result.append(digits[digit_index])
        digits = digits[digit_index + 1:]
        index -= combo_index - num_of_digit
    result.append(digits[index - 1])
    return format_seq(result)


if __name__ == '__main__':
    # print(permutation_itertools(240, 6))
    # print(find_permutation(240, 6))
    print(dynamic_permutations(240, 6))
    # print(permutation_itertools(3240, 7))
    # print(find_permutation(3240, 7))
    # print(dynamic_permutations(3240, 7))
    print(combination_itertools(12, 3, 6))
    print(find_combination(12, 3, 6))
    print(dynamic_combinations(12, 3, 6))
    print(combination_itertools(24, 3, 8))
    print(find_combination(24, 3, 8))
    print(dynamic_combinations(24, 3, 8))
    print(combination_itertools(112, 4, 9))
    print(find_combination(112, 4, 9))
    print(dynamic_combinations(112, 4, 9))
