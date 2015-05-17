
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

    def get_regular_groups(self, grid, min=3):
        """Return all row and column groups."""
        row_groups = self._get_row_groups(grid.grid, models.patterns.RowPattern, min)
        col_groups = self._get_row_groups(grid.grid.T, models.patterns.ColumnPattern, min)
        return row_groups + col_groups

    def _get_row_groups(self, array, pattern, min):
        """Return groups with a min size that exist with grid on x-axis."""
        groups = []

        for row, col in zip(array, xrange(len(array))):
            start = 0

            while start + min <= len(row):
                size = 1
                orb_type = type(row[start])

                for cell in xrange(start + 1, len(row)):
                    if orb_type != type(row[cell]):
                        break
                    size += 1
                    start += 1

                if size >= min:
                    groups.append(pattern(
                        orb_type, size, (col, start - size + 1)
                    ))

                start += 1

        return groups
