import random

from game import Game, GameStatus
from player import Player

from config import get_config


def run():
    config = get_config()
    game = Game(int(config["GAME_FIELD_SIZE"]))
    symbols_for_game = random.sample(config['PLAYER_SYMBOLS'], int(config['COUNT_PLAYERS']))
    colors_for_game = random.sample(config['COLORS'], int(config['COUNT_PLAYERS']))
    human_player = Player(symbols_for_game[0], colors_for_game[0], is_human=True)
    while human_player.name is None:
        name = input("Введите ваше имя ")
        if len(name) > 0:
            human_player.name = name
        else:
            print("Имя не может быть пустым")
    computer_player = Player(symbols_for_game[1], colors_for_game[1])
    computer_player.name = config["BOT_NAME"]
    game.add_player(human_player)
    game.add_player(computer_player)
    while game.status == GameStatus.IN_PROGRESS:
        game.step()


if __name__ == "__main__":
    run()
