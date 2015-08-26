from random import randint

def shuffle(seq):
    while seq:
        yield seq.pop(randint(0, len(seq)-1))
    
# Test it 5 times
for _ in range(5):
    print(list(shuffle(list(range(10)))))

print(list(shuffle('apple blackberry cherry dragonfruit grapefruit kumquat mango nectarine persimmon raspberry raspberry'.split())))
print(list(shuffle('a e i o u'.split())))