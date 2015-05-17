
import models.cursors


KEYSTROKES = {
    "w": models.cursors.UP,
    "a": models.cursors.LEFT,
    "s": models.cursors.DOWN,
    "d": models.cursors.RIGHT
}


def handle_keystroke_direction(keystroke):
    """Returns direction associated with keystroke."""
    return KEYSTROKES.get(keystroke)
