from util import Point
import sys

class Chester():
    def __init__(self):
        self.pos = Point(0.5, 0.5)
        self.distance_run = 0.0
    
    def distance_to(self, treat):
        dist_vector = self.pos - treat
        return abs(dist_vector)
    
    def find_closest_treat(self, treats):
        closest = treats[0]
        dist_closest = self.distance_to(closest)
        for treat in treats:
            if abs(treat.x - closest.x) + abs(treat.y - closest.y) > dist_closest * 2: continue
            if self.distance_to(treat) < dist_closest:
                closest = treat
                dist_closest = self.distance_to(closest)
        return closest
    
    def run_to(self, treat):
        self.distance_run += self.distance_to(treat)
        self.pos = treat
    
    def gobble(self, treats):
        while len(treats):
            treat = self.find_closest_treat(treats)
            self.run_to(treat)
            treats.remove(treat)
        return self.distance_run


for test in sys.argv[1:]:
    print(test)
    with open(test, 'r') as f:
        num_treats = int(f.readline())
        treats = []
        for item in range(num_treats):
            treat = list(map(float, f.readline().split()))
            treats.append(Point(treat[0], treat[1]))
            
    print(Chester().gobble(treats))
