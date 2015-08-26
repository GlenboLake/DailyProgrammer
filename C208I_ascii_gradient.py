'''
http://www.reddit.com/r/dailyprogrammer/comments/3104wu/20150401_challenge_208_intermediate_ascii/

Input:
  <width> <height>
  <gradient>
  <parameters>

parameters can be "radial x y r" or "linear x1 y1 x2 y2"

examples:
  40 30
   .,:;xX&@
  radial 20 15 20

  60 30
   '"^+$
  linear 30 30 0 0
'''
import sys


def display(grid):
    for row in grid:
        print(''.join(row))

dist = lambda x1, y1, x2, y2: ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
dot = lambda x1a, y1a, x1b, y1b,x2a, y2a, x2b, y2b: (x1b-x1a)*(x2b-x2a)+(y1b-y1a)*(y2b-y2a) 


#######
with open('input/gradient.in') as f:
    width, height = list(map(int, f.readline().split()))
    palette = list(f.readline().rstrip('\n'))
    params = f.readline().split()

grid = [ [''] * width for _ in range(height) ]
gradType = params[0]
if gradType == 'radial':
    cx = int(params[1])
    cy = int(params[2])
    r = int(params[3])
elif gradType == 'linear':
    x1 = int(params[1])
    y1 = int(params[2])
    x2 = int(params[3])
    y2 = int(params[4])
else: raise ValueError

for y in range(height):
    for x in range(width):
        if gradType == 'radial':
            d = dist(x, y, cx, cy)
            char = round(d / r * len(palette))
            char = int(max(0, min(char, len(palette) - 1)))
            grid[y][x] = palette[char]
        elif gradType == 'linear':
            d = dist(x1, y1, x2, y2)
            d1 = dist(x, y, x1, y1)
            d2 = dist(x, y, x2, y2)
            # Goal: Find cos(theta), where theta = acos( (u.v)(|u||v|) )
            a = dot(x1,y1,x,y,x1,y1,x2,y2)/(d*d1)
            char = round(a*d1/d*len(palette))
            char = int(max(0, min(char, len(palette) - 1)))
            grid[y][x] = palette[char]

display(grid)
    
