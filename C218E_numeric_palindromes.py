from _collections import defaultdict
def is_palindrome(value):
    v = value if isinstance(value, str) else str(value)
    return v[::-1] == v

def print_palindromic(number):
    value, steps = palindromic(number)
    if value:
        print('{} gets palindromic after {} steps: {}'.format(number, steps, value))
    else:
        print('{} did not converge after {} steps'.format(number, steps))

def palindromic(number):
    rep = str(number)
    value = int(number)
    steps = 0
    while not is_palindrome(value) and steps < 10000:
        value = value + int(rep[::-1])
        rep = str(value)
        steps += 1
    if not is_palindrome(value): value = None
    return value, steps

def bonuses():
    final = defaultdict(list)
    for n in range(1, 1001):
        value, _ = palindromic(n)
        if value:
            final[value].append(n)
        else:
            print('{} did not converge!'.format(n))
    for value, inputs in final.items():
        if len(inputs) > 1:
            print('{} yielded by {} items: {}'.format(value, len(inputs), ', '.join(map(str, inputs))))
    
print_palindromic(123)
print_palindromic(286)
print_palindromic(196196871)
bonuses()