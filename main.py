import config
from game import Game, GameStatus
from player import Player


def run():
    game = Game(config.GAME_FIELD_SIZE)
    human_player = Player(is_human=True)
    while human_player.name is None:
        name = input("Введите ваше имя ")
        if len(name) > 0:
            human_player.name = name
        else:
            print("Имя не может быть пустым")
    computer_player = Player()
    computer_player.name = config.BOT_NAME
    game.add_player(human_player)
    game.add_player(computer_player)
    game.change_step_order()
    while game.status == GameStatus.IN_PROGRESS:
        game.step()


if __name__ == "__main__":
    run()
