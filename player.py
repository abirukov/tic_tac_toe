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
