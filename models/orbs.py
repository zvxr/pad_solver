
# ANSI escape coloring
RESET="\033[0m"

FOREGROUND_BLACK="\033[30m"
FOREGROUND_RED="\033[31m"
FOREGROUND_GREEN="\033[32m"
FOREGROUND_ORANGE="\033[33m"
FOREGROUND_BLUE="\033[34m"
FOREGROUND_PURPLE="\033[35m"
FOREGROUND_CYAN="\033[36m"
FOREGROUND_LIGHT_GREY="\033[37m"
FOREGROUND_DARK_GREY="\033[90m"
FOREGROUND_LIGHT_RED="\033[91m"
FOREGROUND_LIGHT_GREEN="\033[92m"
FOREGROUND_YELLOW="\033[93m"
FOREGROUND_LIGHT_BLUE="\033[94m"
FOREGROUND_PINK="\033[95m"
FOREGROUND_LIGHT_CYAN="\033[96m"

BACKGROUND_BLACK="\033[40m"
BACKGROUND_RED="\033[41m"
BACKGROUND_GREEN="\033[42m"
BACKGROUND_ORANGE="\033[43m"
BACKGROUND_BLUE="\033[44m"
BACKGROUND_PURPLE="\033[45m"
BACKGROUND_CYAN="\033[46m"
BACKGROUND_LIGHT_GREY="\033[47m"


class Orb(object):
    _background = ""
    _foreground = FOREGROUND_BLACK
    _reset = RESET
    _text = "?"

    @property
    def text(self):
        return self._foreground + self._background + self._text + self._reset

    def select(self, background=BACKGROUND_LIGHT_GREY):
        self._background = background

    def deselect(self):
        self._background = ""


class Fire(Orb):
    _text = "F"
    _foreground = FOREGROUND_RED


class Water(Orb):
    _text = "W"
    _foreground = FOREGROUND_BLUE


class Earth(Orb):
    _text = "E"
    _foreground = FOREGROUND_GREEN


class Light(Orb):
    _text = "L"
    _foreground = FOREGROUND_YELLOW


class Dark(Orb):
    _text = "D"
    _foreground = FOREGROUND_PURPLE


class Heart(Orb):
    _text = "H"
    _foreground = FOREGROUND_PINK
