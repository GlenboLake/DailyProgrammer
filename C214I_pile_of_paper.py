'''
Have you ever layered colored sticky notes in interesting patterns in order to
make pictures? You can create surprisingly complex pictures you can make out of
square/rectangular pieces of paper. An interesting question about these
pictures, though, is: what area of each color is actually showing? We will
simulate this situation and answer that question. Start with a sheet of the
base color 0 (colors are represented by single integers) of some specified
size. Let's suppose we have a sheet of size 20x10, of color 0. This will serve
as our "make_canvas", and first input:
    20 10
We then place other colored sheets on top of it by specifying their color (as
an integer), the (x, y) coordinates of their top left corner, and their
width/height measurements. For simplicity's sake, all sheets are oriented in
the same orthogonal manner (none of them are tilted). Some example input:
    1 5 5 10 3
    2 0 0 7 7 
This is interpreted as:
- Sheet of color 1 with top left corner at (5, 5), with a width of 10 and
  height of 3.
- Sheet of color 2 with top left corner at (0,0), with a width of 7 and height
  of 7.
Note that multiple sheets may have the same color. Color is not unique per
sheet. Placing the first sheet would result in a make_canvas that looks like this:
    00000000000000000000
    00000000000000000000
    00000000000000000000
    00000000000000000000
    00000000000000000000
    00000111111111100000
    00000111111111100000
    00000111111111100000
    00000000000000000000
    00000000000000000000
Layering the second one on top would look like this:
    22222220000000000000
    22222220000000000000
    22222220000000000000
    22222220000000000000
    22222220000000000000
    22222221111111100000
    22222221111111100000
    00000111111111100000
    00000000000000000000
    00000000000000000000
This is the end of the input. The output should answer a single question: What
area of each color is visible after all the sheets have been layered, in order?
It should be formatted as an one-per-line list of colors mapped to their
visible areas. In our example, this would be:
    0 125
    1 26
    2 49
'''
import sys
from collections import Counter
def make_canvas(width, height):
    return [ [0]*width for _ in range(height) ]

def print_canvas(canvas):
    print('\n'.join([''.join(map(str, row)) for row in canvas]))

def lay_paper(canvas, paper):
    color, left, top, width, height = list(map(int, paper.split()))
    for y in range(top, top + height):
        canvas[y][left:left + width] = [color] * width

def lay_papers(canvas, papers):
    for paper in papers:
        lay_paper(canvas, paper)

def print_color_report(canvas):
    d = {}
    for row in canvas:
        for num in row:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
    for k in sorted(d.keys()):
        print(k,d[k])
#--------------------
# dict method

def count_colors(canvas_width, canvas_height, inputs):

    canvas = {}
    for paper in inputs:
        color, left, top, width, height = list(map(int, paper.split()))
        for x in range(left, left+width):
            sys.stdout.write('.')
            sys.stdout.flush()
            for y in range(top, top+height):
                canvas[x,y] = color
    count = Counter()
    for x in range(canvas_width):
        for y in range(canvas_height):
            count[canvas.get((x,y),0)] += 1
    for k,v in sorted(count.items()):
        print(k,v)

def count_colors_memory(width, height, papers):
    pcopy = papers
    pcopy.reverse()
    count = Counter()
    for x in range(width):
        for y in range(height):
            for paper in pcopy:
                color, startx, starty, w, h = list(map(int, paper.split()))
                if x >= startx and x < startx+w and y >= starty and y < starty+h:
                    count[color] += 1
                    break
    for k,v in sorted(count.items()):
        print(k,v)

with open('input/100rects100x100.in') as f:
    w,h = list(map(int, f.readline().split()))
    papers = f.readlines()
count_colors_memory(w, h, papers)