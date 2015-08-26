import string


def mangle_word(word):
    new_word = sorted([letter for letter in word.lower() if letter in string.ascii_lowercase])
    for i, ch in enumerate(word):
        if ch in string.ascii_uppercase:
            new_word[i] = new_word[i].upper()
        elif ch not in string.ascii_letters:
            new_word.insert(i, ch)
    return ''.join(new_word)


def mangle(sentence):
    return ' '.join([mangle_word(word) for word in sentence.split()])

inputs = ["This challenge doesn't seem so hard.",
          'There are more things between heaven and earth, Horatio, than are dreamt of in your philosophy.',
          'Eye of Newt, and Toe of Frog, Wool of Bat, and Tongue of Dog.',
          "Adder's fork, and Blind-worm's sting, Lizard's leg, and Howlet's wing.",
          'For a charm of powerful trouble, like a hell-broth boil and bubble.']
for sentence in inputs:
    print(mangle(sentence))