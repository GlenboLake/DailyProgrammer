"""
http://www.reddit.com/r/dailyprogrammer/comments/3840rp/20150601_challenge_217_easy_lumberjack_pile/
"""
def doit(arg):
    with open(arg) as f:
        size = int(f.readline())
        logs = int(f.readline())
        piles = []
        for _ in range(size):
            piles.extend(list(map(int, f.readline().rstrip().split())))
    for _ in range(logs):
        idx = piles.index(min(piles))
        piles[idx] += 1
    for item in range(size):
        print(' '.join(map(str, piles[item*size:(item+1)*size])))

if __name__ == '__main__':
    for item in range(1,5):
        doit('input/lumberjackC{}.txt'.format(item))