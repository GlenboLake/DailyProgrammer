"""http://www.reddit.com/r/dailyprogrammer/comments/7eh6k8"""
from collections import OrderedDict

sample = '11325992321982432123259'


def count(sequence, length):
    seq = str(sequence)
    counts = OrderedDict()
    for i in range(len(seq) - length + 1):
        key = seq[i:i + length]
        try:
            counts[key] += 1
        except KeyError:
            counts[key] = 1
    return {k: v for k, v in counts.items() if v > 1}


def solve(sequence):
    length = 1
    counts = OrderedDict()
    while True:
        length += 1
        result = count(sequence, length)
        if not result:
            break
        result.update(counts)
        counts = result
    return dict_str(counts) or '0'


def dict_str(d):
    return ' '.join(f'{k}:{v}' for k, v in d.items())


if __name__ == '__main__':
    ins = [82156821568221, 11111011110111011, 98778912332145, 124489903108444899]
    outs = [
        '8215682:2 821568:2 215682:2 82156:2 21568:2 15682:2 8215:2 2156:2 1568:2 5682:2 821:2 215:2 156:2 568:2 682:2 82:3 21:3 15:2 56:2 68:2',
        '11110111:2 1111011:2 1110111:2 111101:2 111011:3 110111:2 11110:2 11101:3 11011:3 10111:2 1111:3 1110:3 1101:3 1011:3 0111:2 111:6 110:3 101:3 011:3 11:10 10:3 01:3',
        '0',
        '44899:2 4489:2 4899:2 448:2 489:2 899:2 44:3 48:2 89:2 99:2']
    for in_, out in zip(ins, outs):
        assert solve(in_) == out, f'\n{solve(in_)}\nis not\n{out}'
