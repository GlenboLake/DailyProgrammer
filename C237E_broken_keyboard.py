import re


def broken_keyboard(keys):
    return max(re.findall(r'\b[' + keys + r']+\b', open('input/enable1.txt').read()), key=len)

while True:
    keys = input()
    if not keys:
        break
    print(broken_keyboard(keys))