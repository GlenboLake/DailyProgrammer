def heighway_sequence(degree):
    if degree == 1:
        return 'L'
    else:
        first = heighway_sequence(degree - 1)
        second = ''.join(['L' if turn == 'R' else 'R' for turn in first[::-1]])
        return first + 'L' + second

def heighway(degree):
    directions = [(1,0), (0,1), (-1,0),(0,-1)]
    d = 0  # Initial direction: (1,0) = +1 x axis
    points = [(0,0), (1,0)]
    here = (1,0)
    for turn in heighway_sequence(degree):
        d += 1 if turn == 'L' else -1
        d %= 4
        here = (here[0]+directions[d][0], here[1]+directions[d][1])
        points.append(here)
    return points


points = heighway(12)
print(points)
print((sum([p[0] for p in points])))
print((sum([p[1] for p in points])))