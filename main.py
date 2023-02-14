import random

from game import Game, GameStatus
from player import Player

from config import get_config


def run():
    config = get_config()
    game = Game(int(config.game_field_size))
    human_symbol, computer_symbol = random.sample(config.player_symbols, int(config.count_players))
    human_color, computer_color = random.sample(config.colors, int(config.count_players))
    human_player = Player(human_symbol, human_color, is_human=True)
    while human_player.name is None:
        name = input("Введите ваше имя ")
        if len(name) > 0:
            human_player.name = name
        else:
            print("Имя не может быть пустым")
    computer_player = Player(computer_symbol, computer_color)
    computer_player.name = config.bot_name
    game.add_player(human_player)
    game.add_player(computer_player)
    while game.status == GameStatus.IN_PROGRESS:
        game.step()


if __name__ == "__main__":
    run()
