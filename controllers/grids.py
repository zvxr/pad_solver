"""Includes methods for generating and manipulating grids."""

import controllers.orbs
import models.grids



def generate_random_grid():
    """Returns a random grid."""
    return models.grids.Grid([[controllers.orbs.get_random_orb() for x in xrange(6)] for x in xrange(5)])
