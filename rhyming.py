"""
Challenge 263-intermediate: get rhyming words
https://www.reddit.com/r/dailyprogrammer/comments/4fnz37
"""


def get_rhyme(word):
    global words, phenomes
    pronunciation = words[word]
    index = [phenomes[x.rstrip('012')] for x in pronunciation[::-1]].index('vowel')
    return pronunciation[-index - 1:]


def matching_phenomes(other):
    global word
    this = words[word].copy()
    that = words[other].copy()
    count = 0
    while this.pop() == that.pop():
        count += 1
        if not this or not that:
            break
    return count


with open('input/phenomes.txt') as f:
    phenomes = dict([tuple(line.split('\t')) for line in f.read().splitlines()])
with open('input/rhyming_dictionary.txt') as f:
    words = [line.split('  ') for line in f.read().splitlines() if not line.startswith(';;;')]
    words = {word: sounds.split() for word, sounds in words}

word = 'SOLUTION'
rhyme_sound = get_rhyme(word)

# TODO: change len(p) to calculate matching phenomes
rhymes = [(matching_phenomes(w), w, ' '.join(p)) for w, p in words.items()
          if p[-len(rhyme_sound):] == rhyme_sound
          and w != word]
rhymes = sorted(rhymes, key=lambda x: x[1])
rhymes = sorted(rhymes, key=lambda x: -x[0])
rhyme_text = ['[{}] {}\t{}'.format(*r) for r in rhymes]
for i in range(4):
    print(rhyme_text[i])
print('...')
for i in range(-4, 0):
    print(rhyme_text[i])
