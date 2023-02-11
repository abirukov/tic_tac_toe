import config
import random


def is_valid_coords(coord_x: int, coord_y: int) -> bool:
    return 0 <= coord_x < config.GAME_FIELD_SIZE and 0 <= coord_y < config.GAME_FIELD_SIZE


class Player:
    def __init__(self, is_human=False):
        self.symbol = None
        self.name = None
        self.is_human = is_human

    def set_symbol(self, symbol: str) -> None:
        self.symbol = symbol

    def set_name(self, name: str) -> None:
        self.name = name

    def get_step_coords(self, empty_cells: list[tuple]) -> tuple:
        if not self.is_human:
            coords = random.choice(empty_cells)
        else:
            correct_input = False
            max_range = config.GAME_FIELD_SIZE - 1
            while not correct_input:
                coord_x = int(input(f"Введите координату по горизонтали (от 0 до {max_range} слева направо)"))
                coord_y = int(input(f"Введите координату по вертикали (от 0 до {max_range} сверху вниз)"))
                if empty_cells.count((coord_x, coord_y)):
                    coords = (coord_x, coord_y)
                    correct_input = True
                elif is_valid_coords(coord_x, coord_y):
                    print('Координаты  ошибочны')
                else:
                    print('Клетка уже занята')
        return coords
