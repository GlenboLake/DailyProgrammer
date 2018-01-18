"""http://www.reddit.com/r/dailyprogrammer/comments/7cnqtw"""

challenges = ['IKEUNFUVFV',
              'PXLJOUDJVZGQHLBHGXIW',
              '*l1J?)yn%R[}9~1"=k7]9;0[$']


def find_recurring_a(s):
    try:
        character = s[min(s.index(ch) for ch in s if s.count(ch) > 1)]
        return f'{character} at {s.index(character)}'
    except ValueError:
        return "Nothing recurred"


def find_recurring_b(s):
    try:
        character = s[min(s.index(ch, s.index(ch) + 1) for ch in s if s.count(ch) > 1)]
        return f'{character} at {s.index(character)}'
    except ValueError:
        return "Nothing recurred"


if __name__ == '__main__':
    for c in challenges:
        print(find_recurring_a(c), '-', find_recurring_b(c))
