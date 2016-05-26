import random

difficulty = input('Difficulty (1-5)? ')
while difficulty not in map(str, range(1, 6)):
    difficulty = input('Difficulty (1-5)? ')

difficulty_value = random.choice({
    '1': [4, 5, 6],
    '2': [7, 8, 9],
    '3': [10, 11],
    '4': [12, 13],
    '5': [14, 15]
}[difficulty])
wordlist = open('input/enable1.txt').read().splitlines()
words = [word for word in wordlist if len(word) == difficulty_value]
options = []
for _ in range(difficulty_value + 2):
    word = random.choice(words)
    options.append(word.lower())
    words.remove(word)
    if not words:
        # There might not be difficulty+2 words available.
        break
password = random.choice(options)

for word in options:
    print(word.upper())
    
tries = 4
guess = ''
while tries and guess != password:
    guess = input('Guess ({} left)? '.format(tries)).lower()
    if guess not in options:
        print('Invalid guess')
        continue
    count = sum(a==b for a,b in zip(guess, password))
    print('{}/{} correct'.format(count, difficulty_value))
    tries -= 1
if guess == password:
    print('You win!')
else:
    print('You lose!')
    print('The answer was', password)