
import numpy as np


X_SIZE = 5
Y_SIZE = 6
XY_SIZE = X_SIZE * Y_SIZE


class Grid(object):
    """Wraps numpy array type, shaped as 2-d array.
    """
    HORIZONTAL_DELIMITER = " "
    VERTICAL_DELIMITER = "\n"

    def __init__(self, values):
        """values should contain 30 orbs."""
        if len(values) != XY_SIZE:
            raise Exception("Grid must consist of %s values." % XY_SIZE)
        self.grid = np.array(values)
        self.grid.shape = (X_SIZE, Y_SIZE)

    def __str__(self):
        """simple single letter text representation of grid."""
        return self.VERTICAL_DELIMITER.join([
            self.HORIZONTAL_DELIMITER.join([
                orb.text for orb in row
            ]) for row in self.grid
        ])
