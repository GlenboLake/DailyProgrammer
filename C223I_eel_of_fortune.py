import itertools
import string


wordlist = open('input/enable1.txt').read().splitlines()

def problem(secret, offensive):
    return ''.join([letter for letter in secret if letter in offensive]) == offensive


def problem_count(offensive):
    count = 0
    for word in wordlist:
        if problem(word, offensive):
            count += 1
    return count

print(problem_count('snond'))
print(problem_count('rrizi'))

combos = itertools.product(*([string.ascii_lowercase] * 5))
counts = {}
progress = 0
for combo in combos:
    word = ''.join(combo)
    progress += 1
    if progress % 1e3 == 0:
        print(word)
    counts[word] = problem_count(word)
top_ten = sorted(iter(counts.items()), key=lambda x: x[1], reverse=True)[:10]
print(top_ten)
