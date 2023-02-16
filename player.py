from dataclasses import dataclass

from game_enums import Color


@dataclass
class Player:
    symbol: str
    color: Color
    is_human: bool = False
    name: str | None = None

    def input_name(self):
        while self.name is None:
            name = input("Введите ваше имя ")
            if len(name) > 0:
                self.name = name
            else:
                print("Имя не может быть пустым")


def set_names_for_players(players: list[Player], bot_name: str) -> None:
    for player_index, player in enumerate(players, start=1):
        if player.is_human:
            player.input_name()
        else:
            player.name = f"{bot_name}_{player_index}"
