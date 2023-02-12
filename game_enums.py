from enum import Enum

import config


class GameStatus(Enum):
    IN_PROGRESS = "IN_PROCESS"
    GAME_OVER = "GAME_OVER"


class Symbol(Enum):
    CROSS = config.SYMBOLS[0]
    ZERO = config.SYMBOLS[1]


class Color(Enum):
    FIRST = config.COLORS[0]
    SECOND = config.COLORS[1]
