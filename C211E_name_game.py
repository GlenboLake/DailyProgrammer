'''
Come on everybody!
I say now let's play a game
I betcha I can make a rhyme out of anybody's name

The first letter of the name, I treat it like it wasn't there
But a "B" or an "F" or an "M" will appear
And then I say "bo", add a "B", then I say the name
and "Bonana fanna" and a "fo"

And then I say the name again with an "F" very plain
and a "fee fy" and a "mo"
And then I say the name again with an "M" this time
and there isn't any name that I can't rhyme
But if the first two letters are ever the same,
I drop them both and say the name like

Bob, Bob drop the B's "Bo-ob"
For Fred, Fred drop the F's "Fo-red"
For Mary, Mary drop the M's Mo-ary
That's the only rule that is contrary.
'''
vowels = 'aeiouAEIOU'

def name_game(name):
    name = name.rstrip('!')
    base = name[1:] if name[0] not in vowels else name.lower()
    b = base if name[0] == 'B' else 'B'+base
    f = base if name[0] == 'F' else 'F'+base
    m = base if name[0] == 'M' else 'M'+base
    
    print('''{0}, {0} bo {1},
Bonana fanna fo {2},
Fee fy mo {3},
{0}!'''.format(name, b, f, m))
    print()

name_game('Lincoln!')
name_game('Nick!')
name_game('Arnold!')
name_game('Billy!')