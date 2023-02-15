import logging
import random

from game import Game, GameStatus
from player import Player

from config import get_config

logging.basicConfig(level=logging.INFO, filename="game_log.log", filemode="w",
                    format="%(asctime)s %(message)s")


def run():
    config = get_config()
    game = Game(int(config.game_field_size))
    human_symbol, computer_symbol = random.sample(config.player_symbols, int(config.count_players))
    human_color, computer_color = random.sample(config.colors, int(config.count_players))
    human_player = Player(symbol=human_symbol, color=human_color, is_human=True)
    human_player.input_name()
    computer_player = Player(symbol=computer_symbol, color=computer_color)
    computer_player.name = config.bot_name
    game.add_player(human_player)
    game.add_player(computer_player)
    while game.status == GameStatus.IN_PROGRESS:
        game.step()


if __name__ == "__main__":
    run()
