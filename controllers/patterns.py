
"""For recognizing patterns within a grid.
"""

import inspect
import models.patterns


def common_bases(seq):
    """http://stackoverflow.com/questions/13252333/python-check-if-all-elements-of-a-list-are-the-same-type"""
    iseq = iter(seq)
    bases = set(inspect.getmro(type(next(iseq))))
    for item in iseq:
        bases = bases.intersection(inspect.getmro(type(item)))
        if not bases:
           break
    return bases

class Session(object):
    def __init__(self, *patterns):
        """Accepts any number of Pattern instances."""
        # Validate.
        for pattern in patterns:
            if type(pattern) != models.patterns.Pattern:
                raise TypeException("Session only initialized with Pattern instances.")

        self.patterns = patterns

    def _get_row_groups(self, grid, min=3):
        """Return groups with a min size that exist with grid on x-axis."""
        groups = []
        for col in xrange(len(grid.grid) / len(grid.grid[0]) + 1):
            row = grid.grid[col]
            for offset in xrange(len(row) / min + 1):
                if offset + min > len(row):
                    break
                if len(set([type(cell) for cell in row[offset:offset + min]])) == 1:
                    groups.append((col, row[offset]))
            # TODO: Handle where len(row) / min > 1.0
        return groups
