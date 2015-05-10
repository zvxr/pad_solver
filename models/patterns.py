

class Pattern(object):
    """Patterns are linear sets of orbs that will trigger a match.
    """
    SIZES = (3, 4, 5, 6)

    def __init__(self, size, orb):
        self.size = size
        self.orb = orb
