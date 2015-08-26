import string

weights = {k: v + 1 for k, v in zip(string.ascii_uppercase, list(range(26)))}

word = input('word: ').upper()
while word:
    for i in range(1, len(word)):
        head_weight = sum((idx + 1) * weights[letter]
                          for idx, letter in enumerate(word[i - 1::-1]))
        tail_weight = sum((idx + 1) * weights[letter]
                          for idx, letter in enumerate(word[i + 1:]))
        if head_weight == tail_weight:
            break
    if i == len(word) - 1:
        print(word, 'DOES NOT BALANCE')
    else:
        print(word[:i], word[i], word[i + 1:], '-', head_weight)
    word = input('word: ').upper()
