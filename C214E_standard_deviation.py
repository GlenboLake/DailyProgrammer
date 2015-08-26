from math import sqrt

def stddev(items):
    items = [float(x) for x in items]
    avg = sum(items)/len(items)
    var = sum([(x-avg)**2 for x in items])/len(items)
    return sqrt(var)

def numlist(s):
    return [int(x) for x in s.split(' ')]

print(stddev('5 6 11 13 19 20 25 26 28 37'.split()))
print(stddev('37 81 86 91 97 108 109 112 112 114 115 117 121 123 141'.split()))