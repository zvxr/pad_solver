SIZES = (3, 4, 5, 6)


class Pattern(object):
    """Patterns are linear sets of orbs that will trigger a match.
    """
    def __init__(self, orb_type, size):
        self.orb_type = orb_type
        self.size = size

    def __str__(self):
        """String representation more for debugging. '{orb_type}({size})'"""
        return "{0}({1})".format(self.orb_type, self.size)
