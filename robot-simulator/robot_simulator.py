from collections import namedtuple, deque

Point = namedtuple('Point', ['x', 'y'])

#Bearings also dub as point deltas for orientation
NORTH = Point(x=0, y=1)
EAST = Point(x=1, y=0)
SOUTH = Point(x=0, y=-1)
WEST = Point(x=-1, y=0)

class Robot(object):
    __bearings = deque([NORTH, EAST, SOUTH, WEST])

    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.__coordinates = Point(x, y)
        self.__sim_instr_handlers = {
            'L': self.turn_left,
            'R': self.turn_right,
            'A': self.advance,
        }

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, value):
        self.__coordinates = value

    @property
    def bearing(self):
        return self.__bearings[0]

    @bearing.setter
    def bearing(self, value):
        while value != self.bearing:
            self.turn_right()

    def turn_right(self):
        self.__bearings.rotate(-1)

    def turn_left(self):
        self.__bearings.rotate(1)

    def advance(self):
        dx, dy = self.bearing
        cx, cy = self.coordinates
        self.coordinates = Point(x=cx + dx, y=cy + dy)

    def simulate(self, instructions):
        for instr in instructions:
            self.__sim_instr_handlers[instr]()
