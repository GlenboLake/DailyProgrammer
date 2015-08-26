'''
http://www.reddit.com/r/dailyprogrammer/comments/33hwwf/20150422_challenge_211_intermediate_ogre_maze/

Today we are going to solve a maze. What? Again? Come on, Simpsons did it. Yah
okay so we always pick a hero to walk a maze. This time our hero is an Ogre.
An ogre is large. Your run of the mill hero "@" takes up a 1x1 spot. Easy. But
our beloved hero today is an ogre.
  @@
  @@
Ogres take up a 2x2 space instead of a 1x1. This makes navigating a maze
tougher as you have to handle the bigger ogre. So I will give you a layout of a
swamp. (Ogres navigate swamps while puny heroes navigate caves. That's the
unwritten rules of maze challenges) You will find the path (if possible) for
the ogre to walk to his gold.

Input:

You will read in a swamp. The swamp is laid out in 10x10 spaces. Each space can
be the following:
  . - empty spot
  @ - 1/4th of the 2x2 ogre
  $ - the ogre's gold
  O - sink hole - the ogre cannot touch these. All 2x2 of the Ogre manages to
      fall down one of these (even if it is a 1x1 spot too. Don't be bothered
      by this - think of it as a "wall" but in a swamp we call them sink holes)

Output:

You will navigate the swamp. If you find a path you will display the solution
of all the spaces the ogre will occupy to get to his gold. Use a "&" symbol to
show the muddy path created by the ogre to reach his gold. If there is no path
at all then you will output "No Path"
'''
from util import Direction, Point
from random import randint

OGRE = '@'
EMPTY = '.'
HOLE = 'O'
GOLD = '$'
FOOTPRINT = '&'

def flatten(l):
    '''
    Flatten a list of lists
    '''
    return [item for sublist in l for item in sublist]

class Ogre(object):
    def __init__(self, x, y):
        self.pos = Point(x, y)
        self.direction = Direction.down
    
    def leave_footprint(self, maze):
        maze[self.pos.y]  [self.pos.x]   = \
        maze[self.pos.y]  [self.pos.x+1] = \
        maze[self.pos.y+1][self.pos.x]   = \
        maze[self.pos.y+1][self.pos.x+1] = FOOTPRINT
        
    def current_player(self):
        # He likes turning left.
        self.direction -= 1
    
    def clone(self):
        return Ogre(self.pos.x, self.pos.y)

    def __add__(self, turns):
        if type(turns) is not Direction:
            raise TypeError("Ogres can only move in Directions")
        newpos = self.pos + turns
        return Ogre(newpos.x, newpos.y)

    def __iadd__(self, other):
        new = self + other
        self.pos = new.pos
        self.direction = other
        return self

    def __repr__(self, *args, **kwargs):
        return 'Ogre at {} facing {}'.format(self.pos, self.direction.name)

class Navigator(object):
    def __init__(self, maze):
        if isinstance(maze, str):
            self.maze = list(map(list, maze.split('\n')))
        else:
            self.maze = maze
        self.ogre = self.find_ogre(self.maze)
        self._validate_maze()
        self.divegence_stack = []
        
    def find_ogre(self, maze):
        for y in range(len(maze)):
            for x in range(len(maze[y])):
                if maze[y][x] == OGRE:
                    # Verify other spaces
                    if maze[y + 1][x] == OGRE and \
                       maze[y][x + 1] == OGRE and \
                       maze[y + 1][x + 1] == OGRE:
                        return Ogre(x, y)
                    else: return None
        
    def _validate_maze(self):
        # Check for invalid characters
        chars = set(tile for row in self.maze for tile in row)
        valid = set([OGRE, EMPTY, HOLE, GOLD])
        if chars > valid:
            raise ValueError("Invalid characters detected: " + ','.join(valid))
        if not self.ogre:
            raise ValueError("No ogre...")
        if GOLD not in chars:
            raise ValueError("No gold...")
    
    def print_maze(self):
        for row in self.maze:
            print(''.join(row))

    def is_gold_found(self):
        return GOLD not in set(tile for row in self.maze for tile in row)
    
    def _get_area(self, x, y):
        return [item[x:x+2] for item in self.maze[y:y+2]]
    
    def ogre_can_move(self):
        directions = []
        for d in Direction:
            ogre = self.ogre + d
            area = self._get_area(ogre.pos.x, ogre.pos.y)
            if HOLE not in flatten(area) and len(flatten(area)) is 4:
                # The ogre CAN move in that direction. But should he?
                # Only add the direction if there are non-footprint tiles there
                if set(flatten(area)) != set('&'):
                    directions.append(d)
        return directions
            
    
    def find_gold(self):
        self.ogre.leave_footprint(self.maze)
        while not self.is_gold_found():
            dirs = self.ogre_can_move()
            if len(dirs) > 1:
                self.divegence_stack.append(self.ogre.clone())
                # Favor going straight, then turning left
                while self.ogre.direction not in dirs:
                    self.ogre.current_player()
                d = self.ogre.direction
            elif len(dirs) == 1:
                d = dirs[0]
            elif len(dirs) == 0:
                # Backtrack if we can!
                try:
                    self.ogre = self.divegence_stack.pop()
                    #print 'Got stuck! Backtracking to ({},{})'.format(self.ogre.x, self.ogre.y)
                    continue
                except IndexError:
                    print('No path')
                    return
            self.ogre += d
            self.ogre.leave_footprint(self.maze)
            #print self.ogre
        self.print_maze()
        return


def random_maze(size):
    maze = [ [EMPTY]*size for _ in range(size) ]
    for _ in range(int(size**2*.1)):
        x = randint(0,size-1)
        y = randint(0,size-1)
        maze[x][y] = HOLE
    x = randint(0,size-1)
    y = randint(0,size-1)
    maze[x][y] = GOLD
    x = randint(0,size-2)
    y = randint(0,size-2)
    maze[x][y] = maze[x][y+1] = maze[x+1][y] = maze[x+1][y+1] = OGRE
    return maze

mazes = ['''@@........
@@O.......
.....O.O..
..........
..O.O.....
..O....O.O
.O........
..........
.....OO...
.........$''',
'''@@........
@@O.......
.....O.O..
..........
..O.O.....
..O....O.O
.O........
..........
.....OO.O.
.........$''',
'''$.O...O...
...O......
..........
O..O..O...
..........
O..O..O...
..........
......OO..
O..O....@@
........@@''',
'''.@@.....O.
.@@.......
..O..O....
.......O..
...O......
..........
.......O.O
...O.O....
.......O..
.........$''']

for maze in mazes:
    Navigator(maze).find_gold()
    print()

nav = Navigator(random_maze(20))
nav.print_maze()
print('==== NAVIGATING ====')
nav.find_gold()
