

class Grid(object):
    """The grid is a 6x5 area that contains orbs.
    """
    HORIZONTAL_DELIMITER = " "
    VERTICAL_DELIMITER = "\n"

    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        return self.VERTICAL_DELIMITER.join([
            self.HORIZONTAL_DELIMITER.join([
                orb.text for orb in row
            ]) for row in self.grid
        ])
