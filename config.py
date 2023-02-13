import os
import random
from typing import Mapping, Any

from game_enums import Color
import os
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


def get_config() -> Mapping[str, Any]:
    config = {
        "GAME_FIELD_SIZE": os.environ.get("GAME_FIELD_SIZE", 3),
        "COUNT_PLAYERS": os.environ.get("COUNT_PLAYERS", 2),
        "BOT_NAME": os.environ.get("BOT_NAME", "Бот"),
        "PLAYER_SYMBOLS": os.environ.get("PLAYER_SYMBOLS", "X,O").split(",")
    }
    random.shuffle(config["PLAYER_SYMBOLS"])
    color_values = os.environ.get("COLORS", "yellow,red").split(",")
    color_enums = []
    for color in list(Color):
        if color_values.count(color.value):
            color_enums.append(color)
        config["COLORS"] = color_enums
    return config
