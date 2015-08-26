'''
In this modern fast paced time of the internet it is a busy place for
hardworking unsigned integers (lets just call them ints) Believe it or not
these ints love to date and hook up. But they don't always get along.
Computer scientists have discovered 32 levels of compatibility. By comparing
the binary value of ints we can develop a percentage of compatibility. (these
unsigned integers need 32 bits to store in memory) For today's challenge you
will be given 2 unsigned ints who might be a match. You will compute a
percentage of compatibility by comparing the binary value of each unsigned ints
to each other. For every bit (1 or 0) in common they generate 1 match point.
The max will be 32 the lowest will be 0. You then display the percentage of
compatibility. Also as a service to the unsigned ints you will list the avoid
number. This is the number that is the pure opposite of that number (in binary)
Finding Compatibility:

So for my example I am using 8 bit integers. You must do this for all 32 bits
of an integer. But I am using 8 bit examples to keep it simple.
We are gonna compare 1 and 2
  1 in binary is 0000 0001
  2 in binary is 0000 0010
If you compare each bit place with each number you find that they have 6 bits
in common. (From left to right -- the first 6 bits are all 0 and so the same
bit and so that is 6 match points) the last 2 bits are not the same. They are
different. Therefore 1 and 2 have 6 out of 8 match points. For a compatibility
score of 75%. The most compatible numbers will be the same number as all the
bits match perfectly. (We are all most compatible with ourselves the most)
So taking 1 in binary (0000 0001) the complete opposite number would have to be
(1111 1110) or 254. 1 and 254 should not be in the same data structure together
ever.

Input:
  2 unsigned Integers x and y
Output
  % of compatibility
  x should avoid (x's opposite)
  y should avoid (y's opposite)
'''
BITS = 32
def compatibility(x, y):
    # 1 - (nonmatching count / total bits)
    return int((1 - bin(x ^ y).count('1') / float(BITS)) * 100)

def avoid(x):
    return ~x & (2**BITS-1)
     
def match(x, y):
    print(('{}% Compatibility'.format(compatibility(x, y))))
    print(('{} should avoid {}'.format(x, avoid(x))))
    print(('{} should avoid {}'.format(y, avoid(y))))
    print()

match(20, 65515)
match(32000, 101)
match(42000, 42)
match(13, 12345)
match(9999, 9999)
match(8008, 37331)
match(54311, 2)
match(31200, 34335)