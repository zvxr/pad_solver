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


class RowPattern(Pattern):
    def __init__(self, orb_type, size, head):
        """Represents a row starting at tuple coordinates `head`."""
        super(RowPattern, self).__init__(orb_type, size)
        self.head = head

    def __str__(self):
        """String representation: `{orb_type}({size} starting at {head})`"""
        return "Row {0}({1} starting at {2})".format(self.orb_type, self.size, self.head)


class ColumnPattern(Pattern):
    def __init__(self, orb_type, size, head):
        """Represents a column starting at tuple coordinates `head`."""
        super(ColumnPattern, self).__init__(orb_type, size)
        self.head = head

    def __str__(self):
        """String representation: `{orb_type}({size} starting at {head})`"""
        return "Column {0}({1} starting at {2})".format(self.orb_type, self.size, self.head)
