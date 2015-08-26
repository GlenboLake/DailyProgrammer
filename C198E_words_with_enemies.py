'''
http://www.reddit.com/r/dailyprogrammer/comments/2syz7y/20150119_challenge_198_easy_words_with_enemies/
'''
from string import ascii_lowercase
def war(left, right):
    lscore = []
    rscore = []
    for letter in ascii_lowercase:
        lcount = left.count(letter)
        rcount = right.count(letter)
        if lcount < rcount:
            rscore.extend([letter] * (rcount - lcount))
        elif lcount > rcount:
            lscore.extend([letter] * (lcount - rcount))
    print("left contributed:", ''.join(lscore))
    print("right contributed:", ''.join(rscore))
    print('Winner:', 'LEFT' if len(lscore) > len(rscore) else \
                     'RIGHT' if len(lscore) < len(rscore) else \
                     'TIE')

war('because', 'cause')
war('hello', 'below')
war('hit', 'miss')
war('rekt', 'pwn')
war('combo', 'jumbo')
war('critical', 'optical')
war('isoenzyme', 'apoenzyme')
war('tribesman', 'brainstem')
war('blames', 'nimble')
war('yakuza', 'wizard')
war('longbow', 'blowup')