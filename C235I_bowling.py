def validate_game(game):
    frames = game.split()
    if len(frames) != 10:
        print('All games should be ten frames')
        return False
    for i, frame in enumerate(frames, start=1):
        if len(frame) == 1 and frame != 'X':
            print('Frame', i, 'is invalid: one-ball frames must be strikes')
            return False
        elif i != 10:
            if 'X' in frame and len(frame) > 1:
                print('Cannot have multiple strikes in a normal frame')
                return False
        if len(frame) > (2 + (i == 10)):
            print('Frame', i, 'has too many balls thrown')
            return False
        if frame[0] == '/':
            print('Frame', i, 'begins with a spare')
            return False
        if not all(ball in '-123456789/X' for ball in frame):
            print('Invalid marks in frame', i, '({})'.format(frame))
            return False
        if all(ball in '123456789' for ball in frame):
            if sum(int(ball) for ball in frame) > 9:
                print('Frame', i, 'has an impossibly high score')
                return False
    if len(frames[-1]) == 3:
        if frames[-1][-1] == '/' > 1:
            print('Extra frame is a spare. Impossible!')
            return False
    return True
        

def value(game, ball):
    try:
        return int(game[ball])
    except:
        if game[ball] == '-':
            return 0
        elif game[ball] == 'X':
            return 10
        elif game[ball] == '/':
            return 10 - value(game, ball-1)

def score_game(game):
    if not validate_game(game):
        return None
    total_score = 0
    balls = game.replace(' ', '')
    final = len(balls)
    if len(game.split()[-1]) == 3:
        final -= 1
    for i, ball in enumerate(balls[:final]):
        if ball == 'X':
            try:
                total_score += value(balls, i+1) + value(balls, i+2)
                total_score += 10
            except IndexError:
                pass
        elif ball == '/':
            total_score += 10 - value(balls, i-1)
            total_score += value(balls, i+1)
        else:
            total_score += value(balls, i)
    return total_score
    
print(score_game('X X X X X X X X X XXX'))
for game in open('input/bowling.txt').read().splitlines():
    print(score_game(game))
