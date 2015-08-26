'''
The 1st of April brought the Button to Reddit - if you've not heard of it, read
the blog post on it here. The value of the countdown at the instant that
someone presses the button determines the flair that they obtain on the
subreddit. For example, if the counter is at 53.04 seconds, then I would obtain
a 53 flair, as that is the number of seconds (rounded down). After a person
presses the button, the countdown resets from 60.00 seconds. Today's challenge
is simple - you'll be given a list of users in no particular order, and told at
which time each user pressed the button; you'll need to work out which flair
each user gets. You can assume that the countdown never runs to zero for this
challenge, and that no two users will press the button at exactly the same
moment.

Input example:
  7
  UserA: 41.04
  UserB: 7.06
  UserC: 20.63
  UserD: 54.28
  UserE: 12.59
  UserF: 31.17
  UserG: 63.04
'''
class User(object):
    def __init__(self, string):
        info = string.split(': ')
        self.name = info[0]
        self.time = float(info[1])
        self.flair = None
    
    def __repr__(self):
        return '{}: {}'.format(self.name, self.flair if self.flair else 'no flair')

input1 = '''Coder_d00d: 3.14
Cosmologicon: 22.15
Elite6809: 17.25
jnazario: 33.81
nint22: 10.13
rya11111: 36.29
professorlamp: 31.60
XenophonOfAthens: 28.74'''
input2 = '''bholzer: 101.09
Cosmologicon: 27.45
nint22: 13.76
nooodl: 7.29
nottoobadguy: 74.56
oskar_s: 39.90
Steve132: 61.82'''
    
users = []
for item in input2.splitlines():
    users.append(User(item))
users = sorted(users, key=lambda user: user.time)

time = 0.00
for user in users:
    clock = 60.00 - (user.time - time)
    time = user.time
    user.flair = int(clock)
for user in users:
    print(user)