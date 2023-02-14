import os
import random
from collections import namedtuple

from dotenv import load_dotenv
from game_enums import Color


if os.path.exists(os.path.join(os.path.dirname(__file__), '.env')):
    load_dotenv(os.path.join(os.path.dirname(__file__), '.env'))


def get_config() -> namedtuple:
    Config = namedtuple("Config", "game_field_size count_players bot_name player_symbols colors")
    color_values = os.environ.get("COLORS", "yellow,red").split(",")
    game_colors = []
    for color in color_values:
        try:
            game_colors.append(Color(color))
        except ValueError:
            raise

    game_symbols = os.environ.get("PLAYER_SYMBOLS", "X,O").split(",")
    random.shuffle(game_symbols)
    return Config(
        game_field_size=os.environ.get("GAME_FIELD_SIZE", 3),
        count_players=os.environ.get("COUNT_PLAYERS", 2),
        bot_name=os.environ.get("BOT_NAME", "Бот"),
        player_symbols=game_symbols,
        colors=game_colors
    )
