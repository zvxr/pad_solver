
"""Cursor module.
"""

# Syntactic sugar
UP = 'up'
DOWN = 'down'
LEFT = 'left'
RIGHT = 'right'


class Cursor(object):
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    @property
    def position(self):
        return (self.x, self.y)

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value

    def move(self, direction):
        if direction == UP:
            self.x -= 1
        elif direction == RIGHT:
            self.y -= 1
        elif direction == DOWN:
            self.x += 1
        elif direction == LEFT:
            self.y += 1
