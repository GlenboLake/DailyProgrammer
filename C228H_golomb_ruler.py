import itertools

def diffs_in_ruler(ruler):
    diffs = []
    for i,a in enumerate(ruler[:-1]):
        for b in ruler[i+1:len(ruler)]:
            diffs.append(abs(a-b))
    return sorted(diffs)

def validate(ruler):
    diffs = diffs_in_ruler(ruler)
    return len(diffs) == len(set(diffs))

def golomb(order):
    length = sum(range(order))
    yielded = False
    while not yielded:
        for ticks in itertools.combinations(list(range(length+1)), order):
            if validate(ticks):
                yielded = True
                yield ticks
        length += 1
    
order = eval(input('Order: '))
while order:
    order = int(order)
    ruler = sorted(golomb(order))
    print(('length', ruler[0][-1]-ruler[0][0]))
    for r in ruler:
        print((*r))
    order = eval(input('Order: '))