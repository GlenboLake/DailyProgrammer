import random
PIECES = 'IJLOSTZ'

def get_piece():
    if not get_piece.bag:
        get_piece.bag = list(PIECES)
    piece = random.choice(get_piece.bag)
    get_piece.bag.remove(piece)
    return piece
get_piece.bag = None

def validate(result):
    i = 0
    while i < len(result):
        if len(set(result[i:i+7])) != len(result[i:i+7]):
            return 'Invalid'
        i += 7
    return 'Valid'

result = ''.join(get_piece() for _ in range(50))
print(result)
print(validate(result))