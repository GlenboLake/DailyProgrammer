from random import choice

pool = {
        'c': 'bcdfghjklmnpqrstvwxyz',
        'v': 'aeiou'}
pool['C'], pool['V'] = pool['c'].upper(), pool['v'].upper()

print(''.join(choice(pool[ch]) for ch in input()))