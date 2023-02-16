import logging
import random

from game import Game, GameStatus
from player import Player, set_names_for_players

from config import get_config

logging.basicConfig(level=logging.INFO, filename="game_log.log", filemode="w",
                    format="%(asctime)s %(message)s")


def run():
    config = get_config()
    human_symbol, computer_symbol = random.sample(config.player_symbols, int(config.count_players))
    human_color, computer_color = random.sample(config.colors, int(config.count_players))
    players = [
            Player(symbol=human_symbol, color=human_color, is_human=True),
            Player(symbol=computer_symbol, color=computer_color)
        ]
    game = Game(
        int(config.game_field_size),
        players
    )
    set_names_for_players(players, config.bot_name)
    while game.status == GameStatus.IN_PROGRESS:
        game.step()


if __name__ == "__main__":
    run()
