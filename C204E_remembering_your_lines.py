'''
I didn't always want to be a computer programmer, you know. I used to have
dreams, dreams of standing on the world stage, being one of the great actors
of my generation! Alas, my acting career was brief, lasting exactly as long as
one high-school production of Macbeth. I played old King Duncan, who gets
brutally murdered by Macbeth in the beginning of Act II. It was just as well,
really, because I had a terribly hard time remembering all those lines! For
instance: I would remember that Act IV started with the three witches brewing
up some sort of horrible potion, filled will all sorts nasty stuff, but except
for "Eye of newt", I couldn't for the life of me remember what was in it! Today,
with our modern computers and internet, such a question is easy to settle: you
simply open up the full text of the play and press Ctrl-F (or Cmd-F, if you're
on a Mac) and search for "Eye of newt".

And, indeed, here's the passage:
    Fillet of a fenny snake,
    In the caldron boil and bake;
    Eye of newt, and toe of frog,
    Wool of bat, and tongue of dog,
    Adder's fork, and blind-worm's sting,
    Lizard's leg, and howlet's wing,-
    For a charm of powerful trouble,
    Like a hell-broth boil and bubble. 
Sounds delicious!

In today's challenge, we will automate this process. You will be given the full
text of Shakespeare's Macbeth, and then a phrase that's used somewhere in it.
You will then output the full passage of dialog where the phrase appears.
'''
import re
def get_line_number(lines, phrase):
    for row in range(len(lines)):
        if lines[row].find(phrase) >= 0:
            return row


def get_passage(lines, phrase):
    start = get_line_number(lines, phrase)
    end = start + 1
    while lines[start - 1].startswith('    '):
        start -= 1
    while lines[end].startswith('    '):
        end += 1
    passage = '\n'.join(lines[start:end])
    
    speaker = "Spoken by {}:".format(lines[start - 1].strip(' .'))
    
    sceneline = start
    while not lines[sceneline].startswith("SCENE"):
        sceneline -= 1
    scene = lines[sceneline][0:lines[sceneline].index('.')]
    
    actline = sceneline
    while not lines[actline].startswith("ACT"):
        actline -= 1
    act = lines[actline].rstrip('.')
    
    chars = set()
    row = sceneline + 1
    while not (lines[row].startswith("ACT") or lines[row].startswith("SCENE")):
        match = re.match('^  (\w[^.]+)', lines[row])
        if match: chars.add(match.group(1))
        row += 1
    characters = "Characters in scene: " + ', '.join(chars)
    return '\n'.join([act, scene, characters, speaker, passage])


macbeth = [row.strip('\n') for row in open('input/macbeth.txt', 'r').readlines()]
# print get_passage(macbeth, 'break this enterprise')
# print get_passage(macbeth, 'Yet who would have thought')
print(get_passage(macbeth, 'rugged Russian bear'))
