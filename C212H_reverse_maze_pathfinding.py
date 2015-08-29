'''
We recently saw a maze traversal challenge, where the aim is to find the path
through the maze, given the start and end point. Today, however, we're going to
do the reverse. You'll be given the maze, and the path from point A to point B
as a series of steps and turns, and you'll need to find all the potential
candidates for points A and B.

Input: You'll first be given a number N, which is the number of lines of maze
to read. Next, read a further N lines of input, containing the maze - a space
character describes a place in the maze, and any other non-whitespace character
describes a wall.Finally, you'll be given the path through the maze. The path
is contained on a single line, and consists of three possible moves:
- Turn left, represented by the letter l.
- Turn right, represented by the letter r.
- Move forward n spaces, represented by n.
An example path might look like 3r11r9l2rr5, which means to move forward 3
times, turn right, move forward 11 times, turn right, move forward 9 times,
turn left, move forward twice, turn right twice and then move forward 5 times.
This path may start pointing in any direction.

Output: 
Output the set of possible start and end points, like so: (this example doesn't
correspond to the above sample maze.)
  From (0, 0) to (2, 4)
  From (2, 4) to (0, 0)
  From (3, 1) to (5, 5)
This means that, if you were to travel from any of the given start points to
the corresponding end point, the path you take (with the correct initial facing
direction) will be the one given in the input.
(Where (0, 0) is the top-left corner of the maze.)

Sample in:
9
xxxxxxxxx
x       x
xxx x x x
x   x x x
xxx xxx x
x     x x
x xxx x x
x       x
xxxxxxxxx
2r2r2

Sample out:
From (3, 7) to (3, 5)
From (7, 5) to (5, 5)
From (3, 5) to (3, 7)
From (5, 3) to (7, 3)
From (3, 3) to (5, 3)
From (1, 3) to (1, 5)
From (1, 1) to (1, 3)
'''
from enum import Enum


class Direction(Enum):
    up = 0
    right = 1
    down = 2
    left = 3
    __order__ = 'up right down left'
    
    def turn_right(self):
        new_dir = (self.value + 1) % len(Direction)
        return Direction(new_dir)
    
    def turn_left(self):
        new_dir = (self.value - 1) % len(Direction)
        return Direction(new_dir)

class Pathfinder(object):
    
    def __init__(self, maze):
        self.maze = maze
    
    def attempt(self, path, start_row, start_col, start_dir):
        r = start_row
        c = start_col
        d = start_dir
        # Initial check
        if self.maze[r][c] is not ' ': return None
        for step in path:
            if step is 'r':
                d = d.turn_right()
            elif step is 'l':
                d = d.turn_left()
            else:
                dist = int(step)
                for i in range(dist):  # @UnusedVariable
                    r, c = self.move(r, c, d)
                    if self.maze[r][c] is not ' ': return None
        return (c, r)
    
    def move(self, row, col, direction):
        if direction is Direction.up: row -= 1
        if direction is Direction.down: row += 1
        if direction is Direction.left: col -= 1
        if direction is Direction.right: col += 1
        return row, col
    
    def find(self, path):
        for row in range(len(self.maze)):
            for col in range(len(self.maze[row])):
                for start_dir in Direction:
                    end = self.attempt(path, row, col, start_dir)
                    if end:
                        print('{} to {}'.format((col, row), end))
                    
with open('input/maze', 'r') as f:
    rows = int(f.readline())
    maze = []
    for i in range(rows):
        maze.append(f.readline().strip())
    path = f.readline()
# print maze
print(path)
Pathfinder(maze).find(path)
