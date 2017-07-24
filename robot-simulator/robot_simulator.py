from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

#Bearings also dub as point deltas for orientation
NORTH = Point(x=0, y=1)
EAST = Point(x=1, y=0)
SOUTH = Point(x=0, y=-1)
WEST = Point(x=-1, y=0)

class Robot(object):
    _ctl_bearings = [NORTH, EAST, SOUTH, WEST]

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = Point(x, y)

        self._sim_instructions_handler = {
            'L': self.turn_left,
            'R': self.turn_right,
            'A': self.advance,
        }

    def turn_right(self):
        i = self._ctl_bearings.index(self.bearing) - len(self._ctl_bearings)
        self.bearing = self._ctl_bearings[i + 1]

    def turn_left(self):
        i = self._ctl_bearings.index(self.bearing)
        self.bearing = self._ctl_bearings[i - 1]

    def advance(self):
        dx, dy = self.bearing
        cx, cy = self.coordinates
        self.coordinates = Point(x=cx + dx, y=cy + dy)

    def simulate(self, instructions):
        for instr in instructions:
            self._sim_instructions_handler[instr]()
