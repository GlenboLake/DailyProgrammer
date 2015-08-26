'''
Created on May 15, 2015

@author: ghaber
'''
from util import Point, Direction

class Robot(object):
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.pos = Point.origin()
        self.facing = Direction.up
    
    def test_path(self, pathstring):
        self.reset()
        loop_found = False
        # If there's a loop, it will take at most 4 iterations
        for item in range(1,5):
            self._follow_path(pathstring)
            if self.at_start():
                loop_found = True
                break
        if loop_found:
            print('Loop detected! {} cycle(s) to complete loop'.format(item))
        else:
            print('No loop detected!')
            
    def at_start(self):
        return self.facing == Direction.up and self.pos == Point.origin()
    
    def _follow_path(self, pathstring):
        for step in pathstring:
            if step is 'S':
                self._move()
            elif step is 'L':
                self._turn_left()
            elif step is 'R':
                self._turn_right()
        
    def _move(self):
        self.pos += self.facing
    
    def _turn_left(self):
        self.facing -= 1
    
    def _turn_right(self):
        self.facing += 1


rob = Robot()
challenges = ['SRLLRLRLSSS', 'SRLLRLRLSSSSSSRRRLRLR', 'SRLLRLRLSSSSSSRRRLRLRSSLSLS', 'LSRS']
for path in challenges: rob.test_path(path)