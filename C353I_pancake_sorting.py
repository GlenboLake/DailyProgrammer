def show_stack(pancakes):
    print(' '.join(map(str, pancakes)))


def sort(*pancakes):
    flips = 0
    pancakes = list(pancakes)
    # show_stack(pancakes)
    remaining = len(pancakes)
    while remaining:
        biggest = max(pancakes[:remaining])
        pan = pancakes.index(biggest)
        if pan == 0:
            # print('-' * (2*remaining-1))
            pancakes[:remaining] = pancakes[:remaining][::-1]
            while pancakes[remaining-1] == biggest:
                remaining -= 1
                try:
                    biggest = max(pancakes[:remaining])
                except ValueError:
                    break
        else:
            # print('-' * (2*pan+1))
            pancakes[:pan + 1] = pancakes[:pan + 1][::-1]
        flips += 1
        # show_stack(pancakes)
    return flips


if __name__ == '__main__':
    print(sort(3, 1, 2))
    print(sort(7, 6, 4, 2, 6, 7, 8, 7))
    print(sort(11, 5, 12, 3, 10, 3, 2, 5))
    print(sort(3, 12, 8, 12, 4, 7, 10, 3, 8, 10))
