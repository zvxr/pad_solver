"""Includes methods for generating and manipulating grids with cursors.
"""

import controllers.orbs
import models.cursors
import models.grids


def generate_random_grid():
    return models.grids.Grid([controllers.orbs.get_random_orb() for x in xrange(models.grids.XY_SIZE)])


def show_moves(grid, cursor):
    moves = []
    if cursor.x > 0:
        moves.append(models.cursors.UP)
    if cursor.y > 0:
        moves.append(models.cursors.LEFT)
    if cursor.x < models.grids.X_SIZE:
        moves.append(models.cursors.DOWN)
    if cursor.y < models.grids.Y_SIZE:
        moves.append(models.cursors.RIGHT)

    return moves

def swap(grid, cursor, direction):
    """Changes the places of two orbs."""
    from_position = cursor.position
    from_orb = grid.grid[from_position]
    cursor.move(direction)
    to_position = cursor.position
    to_orb = grid.grid[to_position]

    # Make the switch
    grid.grid[to_position] = from_orb
    grid.grid[from_position] = to_orb
