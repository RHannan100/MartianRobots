from robot import Robot


MAXIMUM_X_VALUE = 50
MAXIMUM_Y_VALUE = 50

class Mars:
    """The planet Mars AKA a grid"""

    max_x = 0
    max_y = 0

    robots = []
    def __init__(self, x, y):
        if x <= MAXIMUM_X_VALUE and y <= MAXIMUM_Y_VALUE and x >= 0 and y >= 0:
            self.max_x = x
            self.max_y = y
            return x, y
        else:
            raise ValueError

    def add_robot(self, x, y, orientation):
        self.robots.append(Robot(x, y, orientation))

