import os
import random
from typing import NamedTuple

from dotenv import load_dotenv
from game_enums import Color

if os.path.exists(os.path.join(os.path.dirname(__file__), '.env')):
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


class Config(NamedTuple):
    game_field_size: int
    count_players: int
    bot_name: str
    player_symbols: list[str]
    colors: list[Color]


def get_config() -> Config:
    color_values = os.environ.get("COLORS", "yellow,red").split(",")
    game_colors = []
    for color in color_values:
        game_colors.append(Color(color))
    game_symbols = os.environ.get("PLAYER_SYMBOLS", "X,O").split(",")
    random.shuffle(game_symbols)
    return Config(
        game_field_size=os.environ.get("GAME_FIELD_SIZE", 3),
        count_players=os.environ.get("COUNT_PLAYERS", 2),
        bot_name=os.environ.get("BOT_NAME", "Бот"),
        player_symbols=game_symbols,
        colors=game_colors,
    )
