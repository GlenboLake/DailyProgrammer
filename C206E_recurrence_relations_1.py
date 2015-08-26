from functools import reduce
def recur(init, relation):
    steps = relation.split()
    return reduce(lambda x, step: eval(str(x)+str(step)), steps, init)

def print_recurrence(init, relation, times):
    print('Term 0:', init)
    for i in range(times):
        init = recur(init, relation)
        print('Term {}: {}'.format(i+1, init))

if __name__ == '__main__':
    print_recurrence(1, '*2 +1', 10)
    print()
    print_recurrence(1, '*-2', 8)
