from operator import xor
from functools import reduce


class LFSR(object):
    def __init__(self, taps, func, init):
        self.func = func
        self.state = int(init, 2)
        self.width = len(init)
        self.taps = [self.width - t - 1 for t in taps]

    def _bit(self, b):
        return (self.state & 1 << b) >> b

    def step(self):
        shift = reduce(self.func, (self._bit(t) for t in self.taps)) & 1
        self.state >>= 1
        if shift:
            self.state |= 1 << (self.width - 1)

    def __str__(self):
        return '{:0{}b}'.format(self.state, self.width)


def xnor(a, b):
    return ~xor(a, b)


def run(challenge):
    taps, func, start, count = challenge.split()
    taps = list(map(int, taps[1:-1].split(',')))
    func = xor if func == 'XOR' else xnor
    count = int(count)

    reg = LFSR(taps, func, start)
    print(0, reg)
    for i in range(1, count + 1):
        reg.step()
        print(i, reg)


def periodicity(challenge):
    taps, func, start, count = challenge.split()
    taps = list(map(int, taps[1:-1].split(',')))
    func = xor if func == 'XOR' else xnor

    reg = LFSR(taps, func, start)
    states = set()
    while str(reg) not in states:
        states.add(str(reg))
        reg.step()
    print(len(states))


if __name__ == '__main__':
    for challenge in ['[1,2] XOR 001 7',
                      '[0,2] XNOR 001 7',
                      '[1,2,3,7] XOR 00000001 16',
                      '[1,5,6,31] XOR 00000000000000000000000000000001 16']:
        run(challenge)
        print()
