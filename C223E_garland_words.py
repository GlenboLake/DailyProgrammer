def garland(word):
    degree = 0
    for length in range(1, len(word)):
        if word.endswith(word[:length]):
            degree = length
    return degree

def challenge1(word):
    degree = garland(word)
    if degree > 0:
        s = word
        for _ in range(5):
            s += word[degree:]
        print(s)

print(list(map(garland, ['programmer', 'ceramic', 'onion', 'alfalfa'])))
list(map(challenge1, ['programmer', 'ceramic', 'onion', 'alfalfa']))

print(max(open('input/enable1.txt').read().splitlines(), key=garland))