import os
import random

from game_enums import GameStatus
from player import Player
from termcolor import cprint


class Game:
    def __init__(self, field_size: int):
        self.game_field = [[None for _ in range(field_size)] for _ in range(field_size)]
        self.log = []
        self.players = []
        self.status = GameStatus.IN_PROGRESS

    def add_player(self, player: Player) -> None:
        self.players.insert(random.randint(0, len(self.players)), player)

    def step(self) -> None:
        for player in self.players:
            if self.status != GameStatus.IN_PROGRESS:
                return
            player_step_coords = self.__get_step_coords(player)
            self.__player_step_save(player, player_step_coords)
            self.__check_game_status()
            self.print_game_info()

    def __get_empty_cells(self) -> list[tuple | None]:
        empty_cells = []
        for row_index, row in enumerate(self.game_field):
            for column_index, value in enumerate(row):
                if value is None:
                    empty_cells.append((column_index, row_index))
        return empty_cells

    def __check_game_status(self) -> None:
        winner_symbol = None
        check_winner_results = [
            self.__column_fill_same_symbols(),
            self.__row_fill_same_symbols(),
            self.__diagonal_fill_same_symbols(),
        ]
        for result in check_winner_results:
            if result is not None:
                winner_symbol = result
                break

        if winner_symbol is not None:
            winner = self.__get_player_by_symbol(winner_symbol)
            if winner is not None:
                self.log.append({"message": f"Победил {winner.name}", "color": "magenta"})
            else:
                self.log.append({"message": "Не нашли победителя, обратитесь к разработчику", "color": "magenta"})
            self.status = GameStatus.GAME_OVER
        elif not self.__get_empty_cells():
            self.log.append({"message": "Ничья", "color": "magenta"})
            self.status = GameStatus.GAME_OVER

    def __player_step_save(self, player: Player, step_coords: tuple) -> None:
        self.game_field[step_coords[1]][step_coords[0]] = player.symbol
        self.log.append(
            {
                "message": f"{player.name} поставил {player.symbol} в {step_coords}",
                "color": player.color.value
            }
        )
        cprint(self.log[-1]["message"], self.log[-1]["color"])

    def __column_fill_same_symbols(self) -> str | None:
        result = None
        for column_index in range(len(self.game_field)):
            column = [row[column_index] for row in self.game_field]
            if column.count(column[0]) == len(column):
                result = column[0]
        return result

    def __row_fill_same_symbols(self) -> str | None:
        result = None
        for row in self.game_field:
            if row.count(row[0]) == len(row):
                result = row[0]
        return result

    def __diagonal_fill_same_symbols(self) -> str | None:
        result = None
        left_diagonal = self.__get_diagonal_values()
        if left_diagonal.count(left_diagonal[0]) == len(left_diagonal):
            result = left_diagonal[0]
        right_diagonal = self.__get_diagonal_values(reverse=True)
        if right_diagonal.count(right_diagonal[0]) == len(right_diagonal):
            result = right_diagonal[0]
        return result

    def __get_player_by_symbol(self, symbol: str) -> Player | None:
        for player in self.players:
            if symbol == player.symbol:
                return player
        return None

    def print_game_info(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        for record in self.log:
            cprint(record["message"], record["color"])
        for row in self.game_field:
            printable = "|".join([" " if cell_value is None else cell_value for cell_value in row])
            cprint(printable, "black", "on_white")

    def is_valid_coords(self, coord_x: int, coord_y: int) -> bool:
        return 0 <= coord_x < len(self.game_field[0]) and 0 <= coord_y < len(self.game_field)

    def __get_step_coords(self, player: Player) -> tuple:
        empty_cells = self.__get_empty_cells()
        if not player.is_human:
            coords = random.choice(empty_cells)
        else:
            correct_input = False
            max_range = len(self.game_field) - 1
            while not correct_input:
                try:
                    coord_x = int(input(f"Введите координату по горизонтали (от 0 до {max_range} слева направо) "))
                    coord_y = int(input(f"Введите координату по вертикали (от 0 до {max_range} сверху вниз) "))
                    if empty_cells.count((coord_x, coord_y)):
                        coords = (coord_x, coord_y)
                        correct_input = True
                    elif not self.is_valid_coords(coord_x, coord_y):
                        print('Координаты  ошибочны')
                    else:
                        print('Клетка уже занята')
                except ValueError:
                    print("Ошибка ввода")

        return coords

    def __get_diagonal_values(self, reverse=False) -> list:
        diagonal_values = []
        for row_index, row in enumerate(self.game_field):
            if reverse:
                needle_column_position = len(row) - 1 - row_index
            else:
                needle_column_position = row_index
            diagonal_values.append(self.game_field[row_index][needle_column_position])
        return diagonal_values
