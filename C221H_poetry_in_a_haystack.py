trigrams = {'the': 16, 'and': 15, 'tha': 14, 'ent': 13, 'ing': 12, 'ion': 11, 'tio': 10, 'for': 9,
            'nde': 8, 'has': 7, 'nce': 6, 'edt': 5, 'tis': 4, 'oft': 3, 'sth': 2, 'men': 1}
ONE_LETTER = ['a','o','i']

def score(line):
    one_letter_words = [word for word in line.split() if len(word)==1]
    if any([word for word in one_letter_words if word not in ONE_LETTER]):
        return 0
    else:
        ones = len([word for word in one_letter_words if word in ONE_LETTER])
        return sum([line.count(trigram) * tscore for trigram, tscore in trigrams.items()]) + ones

top_three = ['','','']
top_scores = [0,0,0]
weakest = 0
for line in open('input/poetry.txt').read().splitlines():
    line_score = score(line)
    if line_score > top_scores[weakest]:
        top_scores.append(line_score)
        top_three.append(line)
        top_scores.pop(weakest)
        top_three.pop(weakest)
        weakest = top_scores.index(min(top_scores))
for line in top_three:
    print(line)