def ordinal(n):
    int(str(n))  # To raise an exception if it's not an integer
    if str(n)[-1] == '1' and str(n)[-2:] != '11':
        return '{}st'.format(n)
    elif str(n)[-1] == '2' and str(n)[-2:] != '12':
        return '{}nd'.format(n)
    elif str(n)[-1] == '3' and str(n)[-2:] != '13':
        return '{}rd'.format(n)
    else:
        return '{}th'.format(n)


def placements(place, low=0, high=100):
    for p in range(low, high + 1):
        if p == place:
            continue
        yield ordinal(p)


def print_placement(place, low=0, high=100):
    print(', '.join(placements(place, low, high)))


print_placement(23, low=1, high=150)
