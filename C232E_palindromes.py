import string
from itertools import combinations

# Main problem
def is_palindrome(phrase):
    letters = [ch.lower() for ch in phrase if ch in string.ascii_letters]
    return letters == letters[::-1]

poem = open('input/palindrome.txt').read()
print('Palindrome' if is_palindrome(poem) else 'Not a palindrome')

# Challenge
words = open('input/enable1.txt').read().splitlines()
count = 0
for pair in combinations(words, 2):
    if is_palindrome(''.join(pair)):
        count += 1
        #print(*pair)
print(count)