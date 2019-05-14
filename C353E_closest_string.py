from collections import defaultdict
from itertools import combinations
from textwrap import dedent


def hamming_distance(a, b):
    return sum(x != y for x, y in zip(a, b))


def solve(strings, metric=hamming_distance):
    dists = defaultdict(int)
    for a, b in combinations(strings, 2):
        dist = metric(a, b)
        dists[a] += dist
        dists[b] += dist
    return min(dists, key=lambda val: dists[val])


if __name__ == '__main__':
    sample = ['ATCAATATCAA', 'ATTAAATAACT', 'AATCCTTAAAC', 'CTACTTTCTTT', 'TCCCATCCTTT', 'ACTTCAATATA']
    assert solve(sample) == 'ATTAAATAACT'
    print(solve(dedent('''\
        AACACCCTATA
        CTTCATCCACA
        TTTCAATTTTC
        ACAATCAAACC
        ATTCTACAACT
        ATTCCTTATTC
        ACTTCTCTATT
        TAAAACTCACC
        CTTTTCCCACC
        ACCTTTTCTCA
        TACCACTACTT''').splitlines()))
    print(solve(dedent('''\
        ACAAAATCCTATCAAAAACTACCATACCAAT
        ACTATACTTCTAATATCATTCATTACACTTT
        TTAACTCCCATTATATATTATTAATTTACCC
        CCAACATACTAAACTTATTTTTTAACTACCA
        TTCTAAACATTACTCCTACACCTACATACCT
        ATCATCAATTACCTAATAATTCCCAATTTAT
        TCCCTAATCATACCATTTTACACTCAAAAAC
        AATTCAAACTTTACACACCCCTCTCATCATC
        CTCCATCTTATCATATAATAAACCAAATTTA
        AAAAATCCATCATTTTTTAATTCCATTCCTT
        CCACTCCAAACACAAAATTATTACAATAACA
        ATATTTACTCACACAAACAATTACCATCACA
        TTCAAATACAAATCTCAAAATCACCTTATTT
        TCCTTTAACAACTTCCCTTATCTATCTATTC
        CATCCATCCCAAAACTCTCACACATAACAAC
        ATTACTTATACAAAATAACTACTCCCCAATA
        TATATTTTAACCACTTACCAAAATCTCTACT
        TCTTTTATATCCATAAATCCAACAACTCCTA
        CTCTCAAACATATATTTCTATAACTCTTATC
        ACAAATAATAAAACATCCATTTCATTCATAA
        CACCACCAAACCTTATAATCCCCAACCACAC''').splitlines()))
    jaro('CRATE', 'TRACE')
    jaro('DWAYNE', 'DUANE')
