class Card(object):
    suits = {'S': 'Spades',
             'H': 'Hearts',
             'C': 'Clubs',
             'D': 'Diamonds'}

    values = {
        'A': 1, '2': 2, '3': 3, '4': 4, '5': 5,
        '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'J': 10, 'Q': 10, 'K': 10
    }

    def __init__(self, suit, value):
        if suit not in Card.suits or value not in Card.values:
            raise ValueError
        self.suit = suit
        self.value = value

    def __str__(self):
        return '{} of {}'.format(Card.suits[self.suit], Card.values[self.value])

    def __repr__(self):
        return self.suit + self.value
