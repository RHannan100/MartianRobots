from enum import Enum

ROTATIONS = {
    "L": -1,
    "R": 1
}

class Orientation(Enum):
    N = 0
    E = 1
    S = 2
    W = 3

class Robot:
    """A robot for use on Mars"""

    orientation = Orientation.N
    position_x = 0
    position_y = 0
    lost = False
        
    def __init__(self, x, y, orientation):
        self.position_x = x
        self.position_y = y
        self.set_orientation(orientation)

    def set_orientation(self, orientation):
        self.orientation = Orientation[orientation]

    def get_orientation(self):
        return self.orientation.name

    def get_location(self):
        return {"x": self.position_x, "y": self.position_y}

    def rotate(self, direction):
        new_orientation = self.orientation.value + ROTATIONS[direction]

        if new_orientation == -1:
            new_orientation = 3
        elif new_orientation == 4:
            new_orientation = 0
        
        self.orientation = Orientation(new_orientation)
        return self.position_x, self.position_y

    def forward(self, amount):
        if self.orientation is Orientation.N:
            self.position_y += amount
            return self.get_location()
        elif self.orientation is Orientation.E:
            self.position_x += amount
            return self.get_location()
        elif self.orientation is Orientation.S:
            self.position_y -= amount
            return self.get_location()
        elif self.orientation is Orientation.W:
            self.position_x -= amount
            return self.get_location()
        else:
            return -1

    def move(self, instruction):
        if instruction == "F":
            self.forward(1)
        elif instruction in ["L", "R"]:
            self.rotate(instruction)
        else:
            return -1

    def output_pretty_location(self):
        print("{x} {y} {o} {lost}".format(x = self.position_x, y = self.position_y, o = self.orientation.name, lost = ("", "LOST")[self.lost]))