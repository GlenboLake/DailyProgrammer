"""http://www.reddit.com/r/dailyprogrammer/comments/776lcz"""

from enum import Enum


###### Code from Rubik's project:

class Side(Enum):
    INTERIOR = ' '
    FRONT = 'F'
    BACK = 'B'
    LEFT = 'L'
    RIGHT = 'R'
    UP = 'U'
    DOWN = 'D'

    def __str__(self):
        return self.value

    @classmethod
    def from_s(cls, string):
        try:
            return [s for s in Side if s.value == string][0]
        except IndexError:
            raise ValueError(f"'{string}' is not a valid {cls.__name__}")


side_colors = {
    Side.LEFT: 'O',
    Side.RIGHT: 'R',
    Side.UP: 'W',
    Side.DOWN: 'Y',
    Side.FRONT: 'G',
    Side.BACK: 'B',
    Side.INTERIOR: 'X'
}


class Rotation(Enum):
    X = 1  # R rotation
    Y = 2  # U rotation
    Z = 3  # F rotation
    Xi = -X
    Yi = -Y
    Zi = -Z


class RubiksCube(object):
    def __init__(self):
        # Access is XYZ: (LR, UD, FB)
        self.cubies = [
            [
                [Cubie(*([Side.INTERIOR] * 6))
                 for _ in range(3)]
                for _ in range(3)]
            for _ in range(3)]
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    cubie = self.cubies[x][y][z]
                    if x == 0:
                        cubie.L = Side.LEFT
                    if x == 2:
                        cubie.R = Side.RIGHT
                    if y == 0:
                        cubie.U = Side.UP
                    if y == 2:
                        cubie.D = Side.DOWN
                    if z == 0:
                        cubie.F = Side.FRONT
                    if z == 2:
                        cubie.B = Side.BACK

    def __eq__(self, other):
        if not isinstance(other, RubiksCube):
            return False
        for x in range(3):
            for y in range(3):
                for z in range(3):
                    if self.cubies[x][y][z] != other.cubies[x][y][z]:
                        return False
        return True

    @staticmethod
    def cubie_tuple(name):
        # Validate first
        if not 1 <= len(name) <= 3:
            return None
        if not set(name) < set('LRUDFB'):
            return None
        if 'L' in name and 'R' in name:
            return None
        if 'U' in name and 'D' in name:
            return None
        if 'F' in name and 'B' in name:
            return None
        x = y = z = 1
        if 'L' in name:
            x = 0
        elif 'R' in name:
            x = 2
        if 'U' in name:
            y = 0
        elif 'D' in name:
            y = 2
        if 'F' in name:
            z = 0
        elif 'B' in name:
            z = 2
        return x, y, z

    def __getattr__(self, item):
        coords = self.cubie_tuple(item)
        if coords is None:
            return super().__getattribute__(item)
        else:
            return self.cubies[coords[0]][coords[1]][coords[2]]

    def rotate(self, side):
        if side == Side.LEFT:
            face = ['LUB', 'LU', 'LUF', 'LF', 'LDF', 'LD', 'LDB', 'LB']
            axis = Rotation.Xi
        elif side == Side.RIGHT:
            face = ['RUF', 'RU', 'RUB', 'RB', 'RDB', 'RD', 'RDF', 'RF']
            axis = Rotation.X
        elif side == Side.UP:
            face = ['ULB', 'UB', 'URB', 'UR', 'URF', 'UF', 'ULF', 'UL']
            axis = Rotation.Y
        elif side == Side.DOWN:
            face = ['DLF', 'DF', 'DRF', 'DR', 'DRB', 'DB', 'DLB', 'DL']
            axis = Rotation.Yi
        elif side == Side.FRONT:
            face = ['FUL', 'FU', 'FUR', 'FR', 'FDR', 'FD', 'FDL', 'FL']
            axis = Rotation.Z
        elif side == Side.BACK:
            # face = ['BUR', 'BU', 'BUL', 'BL', 'BDL', 'BD', 'BDR', 'BR']
            face = ['BUL', 'BU', 'BUR', 'BR', 'BDR', 'BD', 'BDL', 'BL']
            axis = Rotation.Zi
        else:
            raise NotImplemented

        # Rotate individual cubies
        cubies = [getattr(self, cubie) for cubie in face]
        for cubie in face:
            getattr(self, cubie).rotate(axis)
        # Put cubies in their new locations
        coords = [self.cubie_tuple(cubie) for cubie in face]
        if axis.name.endswith('i'):
            coords = [coords[i - 2] for i in range(len(coords))]
        else:
            coords = [coords[i - 6] for i in range(len(coords))]
        for cubie, coord in zip(cubies, coords):
            x, y, z = coord
            self.cubies[x][y][z] = cubie

    def execute(self, algorithm):
        steps = algorithm.split()
        for s in steps:
            times = 1
            if len(s) == 2:
                times = {'2': 2, "'": 3}[s[-1]]
            side = Side.from_s(s[0])
            for _ in range(times):
                self.rotate(side)


class Cubie(object):
    def __init__(self, front, back, left, right, up, down):
        self.F = front
        self.B = back
        self.L = left
        self.R = right
        self.U = up
        self.D = down

    def __repr__(self):
        return f'{self.L}{self.R}{self.U}{self.D}{self.F}{self.B}'.replace(' ', '_') or 'C'

    def __eq__(self, other):
        if not isinstance(other, Cubie):
            return False
        return self.F == other.F and \
               self.B == other.B and \
               self.L == other.L and \
               self.R == other.R and \
               self.U == other.U and \
               self.D == other.D

    def rotate(self, axis):
        if axis == Rotation.X:
            self.U, self.B, self.D, self.F = self.F, self.U, self.B, self.D
        elif axis == Rotation.Xi:
            for _ in range(3):
                self.rotate(Rotation.X)
        elif axis == Rotation.Y:
            self.F, self.L, self.B, self.R = self.R, self.F, self.L, self.B
        elif axis == Rotation.Yi:
            for _ in range(3):
                self.rotate(Rotation.Y)
        elif axis == Rotation.Z:
            self.U, self.L, self.D, self.R = self.L, self.D, self.R, self.U
        elif axis == Rotation.Zi:
            for _ in range(3):
                self.rotate(Rotation.Z)


def count_cycles(sequence):
    solved = RubiksCube()
    cube = RubiksCube()
    cycles = 1
    cube.execute(sequence)
    while cube != solved:
        cube.execute(sequence)
        cycles += 1
    return cycles


if __name__ == '__main__':
    print(count_cycles("R"))
    print(count_cycles("R F2 L' U D B2"))
    print(count_cycles("R' F2 B F B F2 L' U F2 D R2 L R' B L B2 R U"))
    print(count_cycles("R U2 R2 U' R U' R' U2 F R F'"))