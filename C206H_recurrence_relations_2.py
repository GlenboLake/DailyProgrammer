from dailyprogrammer.C205I_rpn import evaluate_rpn
import re

cache = {}
#evaluate_rpn

def u(n, rpn):
    #print len(traceback.extract_stack())
    if n in cache:
        return cache[n]
    dependencies = list(map(int, re.findall('\((\d+)\)', rpn)))
    new_rpn = rpn
    for dep in dependencies:
        if n-dep in cache:
            value = cache[n-dep]
        else:
            value = u(n-dep, rpn)
        new_rpn = new_rpn.replace('({})'.format(dep), str(value))
    value = evaluate_rpn(new_rpn)
    cache[n] = value
    return value

if __name__ == '__main__':
    lines = open('input/recurrence2.txt').read().splitlines()
    rule = lines[0]
    max_term = int(lines[-1])
    for k, v in [line.split(':') for line in lines[1:-1]]:
        cache[int(k)] = eval(v)
    for n in range(max_term):
        try:
            value = u(n, rule)
        except:
            # Stack overflow will cause this.
            continue
        print('{}: {}'.format(n, value))
