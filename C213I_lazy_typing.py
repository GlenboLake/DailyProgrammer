'''
We've all had a night where we're so lazy that we actively avoid moving our
hands around on the keyboard. In today's challenge, we'll be given a sentence
to type, and we'll work out a minimal-effort way of typing that string (ie.
minimize how much the hand moves), using a basic QWERTY keyboard layout - the
keys supported are the letters A to Z, shift, and space - in this arrangement:
 qwertyuiop
 asdfghjkl
 ^zxcvbnm ^
    #####
The only letters that can be typed are upper-case and lower-case letters, and
space. Our typist is quite inefficient: they move their fingers around the
keyboard, hunting for keys one by one, so the user only uses one finger of each
hand. The user may start with both hands on any key, and may move either hand
to the next key. The main important things to remember are:
- The user may move to any of the five # (space) positions to type a space.
- Two hands are required to type a capital letter - one must go to a shift key.
  Which hand goes to which key is up to your program to decide, but the same
  hand can't press both the shift key and the letter.
As a score of laziness, you'll also need to work out the total Manhattan
distance (x + y) moved by the hands. We'll call this total distance the effort.
'''
import string
import sys
import re

SHIFT = '^'
SPACE = '#'

valid_chars = string.ascii_letters+SHIFT+SPACE

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += len(sub) # use start += 1 to find overlapping matches

def key_name(key):
    if key in string.ascii_letters:
        return key.upper()
    elif key is '#':
        return 'Space'
    elif key is '^':
        return 'Shift'    

class Keyboard(object):
    def __init__(self, rows):
        self._rows = rows
    
    def find(self, key):
        if key in string.ascii_uppercase: key = key.lower()
        locs = []
        rows = []
        # Find rows with key
        for row in self._rows:
            if key in row:
                rows.append(self._rows.index(row))
        # Find instances of key
        for row in rows:
            places = list(find_all(self._rows[row], key))
            locs.extend([tuple([row,col]) for col in places])
        return locs if len(locs) > 1 else locs[0]

    def key_at(self, row, col):
        return key_name(self._rows[row][col])
    
    def shifts(self):
        return self.find('^')
    
    def spaces(self):
        return self.find('#')

class Hand(object):
    def __init__(self, name, start):
        self.name = name
        self.row = start[0]
        self.col = start[1]
        self.distance = 0
    
    def move_to(self, row, col):
        distance = abs(row-self.row) + abs(col-self.col)
        self.row = row
        self.col = col
        self.distance += distance
        return distance
    
    def distance_to(self, loc):
        return abs(loc[0] - self.row) + abs(loc[1] - self.col)
    
    def choose_closest(self, choices):
        best = None
        for choice in choices:
            if not best:
                best = choice
                dist = self.distance_to(choice)
                continue
            if self.distance_to(choice) < dist:
                best = choice
                dist = self.distance_to(choice)
        return best 

class Navigator(object):
    def __init__(self, keyboard):
        self.keyboard = keyboard
        self.hands = [None, None]
        self.left = None
        self.right = None

    def pick_hand(self, key):
        if not self.hands[0] or not self.hands[1]:
            return None
        loc = self.keyboard.find(key)
        if type(loc) is tuple:
            ldist = self.hands[0].distance_to(loc)
            rdist = self.hands[1].distance_to(loc)
            return self.hands[0] if ldist < rdist else self.hands[1]
        dist = [sys.maxsize, sys.maxsize]
        for l in loc:
            dist[0] = min(dist[0], self.hands[0].distance_to(l))
            dist[1] = min(dist[1], self.hands[1].distance_to(l))
        return self.hands[0] if dist[0] <= dist[1] else self.hands[1]
        
    def travel(self, sentence):
        sentence = sentence.strip()
        sentence = sentence.replace(' ', '#')
        sentence = re.sub('([A-Z])', r'^\1', sentence)
        self.hands = [None, None]
        for letter in sentence:
            if letter not in valid_chars: continue
            
            hand = self.pick_hand(letter)
            location = self.keyboard.find(letter)
            if not hand:
                if not self.hands[0]:
                    print('{}: Use left hand'.format(key_name(letter)))
                    if type(location) is list:
                        location = location[0]
                    self.hands[0] = Hand('left hand', location)
                elif not self.hands[1]:
                    print('{}: Use right hand'.format(key_name(letter)))
                    if type(location) is list:
                        location = location[0]
                    self.hands[1] = Hand('right hand', location)
                continue
            if type(location) is list:
                location = hand.choose_closest(location)
            before = self.keyboard.key_at(hand.row, hand.col)
            effort = hand.move_to(location[0], location[1])
            
            keyname = key_name(letter)
            if effort == 0:
                print('{}: Use {} again'.format(keyname, hand.name))
            else:
                print('{}: Move {} from {} (effort: {})'.format(keyname, hand.name, before, effort))
        print("Total effort:", self.hands[0].distance + self.hands[1].distance)
            
if __name__ == "__main__":
    kb = Keyboard(['qwertyuiop',
              'asdfghjkl',
              '^zxcvbnm ^',
              '   #####'])
    #Navigator(kb).travel('Hello World')
    Navigator(kb).travel('The quick brown Fox')