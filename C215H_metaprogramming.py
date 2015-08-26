# Broken in Python 3
'''
Created on May 22, 2015

@author: ghaber
'''
import types

tests = ['Hello world', '', '0',
         1, 0, 0.0,
         [], [None], [1,2,3],
         True, False, None,
         {}, {None: None}, {0:0}, {1:1},
         (), (0,), (1,2,3)]

def run_tests():
    print('Expression     | Bool')
    print('---------------+-----')
    for t in tests:
        print('{:15} | {}'.format(t.__repr__(), True if t else False))


def test_empty(typename):
    try:
        obj = eval(typename + '()')
    except:
        #print '<failure>       |'
        return
    print('{:15} | {}'.format(obj.__repr__(), True if obj else False))

def test_one_arg(typename):
    try:
        obj = eval(typename + '(1)')
    except:
        #print '<failure>       |'
        return
    print('{:15} | {}'.format(obj, True if obj else False))

print('Expression     | Bool')
print('---------------+-----')
for t in types.__dict__:
    if not t.endswith('Type'): continue
    #print '{:15} |'.format(t[:-4])
    typename = eval('types.'+t).__name__
    test_empty(typename)
    test_one_arg(typename)