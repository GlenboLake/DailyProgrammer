preferences = {}

for line in open('input/stable marriage.txt').read().splitlines():
    person, *prefs = line.split(', ')
    preferences[person] = prefs

def stableMatching():
    available_men = [p for p in preferences if p==p.upper()]
    available_women = [p for p in preferences if p==p.lower()]
    pairs = {}
    while available_men:
        man = available_men[0]
        woman = preferences[man].pop(0)
        if woman in available_women:
            pairs[woman] = man
            available_women.remove(woman)
            available_men.remove(man)
        else:
            rival = pairs[woman]
            if preferences[woman].index(man) < preferences[woman].index(rival):
                available_men.append(rival)
                available_men.remove(man)
                pairs[woman] = man
    return pairs

for k,v in stableMatching().items():
    print('{}: {}'.format(v,k))
