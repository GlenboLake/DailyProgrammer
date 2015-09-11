from itertools import combinations
cards = open('input/set.txt').read().splitlines()

for card_set in combinations(cards, 3):
    if any(len(set(card[i] for card in card_set)) == 2 for i in range(4)):
        continue
    print(*card_set)