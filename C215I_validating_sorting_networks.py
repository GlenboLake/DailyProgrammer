'''
http://www.reddit.com/r/dailyprogrammer/comments/36m83a/20150520_challenge_215_intermediate_validating/
'''


def is_sorted(nums):
    #print 'checking',nums
    for item in range(len(nums)-1):
        if nums[item] > nums[item+1]: return False
    return True


class SortingNetwork(object):
    def __init__(self, wires):
        self.n = wires
        self.connectors = []
    
    def add_connector(self, wires):
        self.connectors.append(wires)

    def sort(self, numbers):
        #print 'sorting',numbers
        for c in self.connectors:
            if numbers[c[0]] > numbers[c[1]]:
                numbers[c[0]], numbers[c[1]] = numbers[c[1]], numbers[c[0]]
        return numbers
    
    def validate(self):
        for item in range(2**self.n):
            nums = list(map(int, list('{0:0{1}b}'.format(item, self.n))))
            if not is_sorted(self.sort(nums)): return False
        return True

with open('input/sorting networks challenge2.txt') as f:
    params = f.readline().split()
    network = SortingNetwork(int(params[0]))
    for _ in range(int(params[1])):
        t = tuple(map(int, f.readline().split()))
        network.add_connector(t)
if network.validate():
    print('Valid network')
else:
    print('Invalid network')