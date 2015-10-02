dictionary = open('input/enable1.txt').read().splitlines()


def spellcheck(word):
    for i in range(len(word)):
        chunk = word[:i + 1]
        if any(w.startswith(chunk) for w in dictionary):
            continue
        return chunk + '<' + word[i + 1:]

words = ['accomodate', 'acknowlegement', 'arguemint', 'comitmment',
         'deductabel', 'depindant', 'existanse', 'forworde', 'herrass',
         'inadvartent', 'judgemant', 'ocurrance', 'parogative', 'suparseed']
for word in words:
    print(spellcheck(word))