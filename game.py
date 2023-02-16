import os
import random

from game_enums import GameStatus
from game_field import GameField
from player import Player
from termcolor import cprint


class Game:
    def __init__(self, field_size: int, players: list[Player]):
        self.game_field = GameField(field_size)
        self.log = []
        self.players = players
        self.status = GameStatus.IN_PROGRESS
        random.shuffle(self.players)

    def step(self) -> None:
        for player in self.players:
            if self.status != GameStatus.IN_PROGRESS:
                return
            player_step_coords = self.__get_step_coords(player)
            self.__player_step_save(player, player_step_coords)
            self.__check_game_status()
            self.print_game_info()

    def __check_game_status(self) -> None:
        winner_symbol = None
        check_winner_results = [
            self.game_field.column_fill_same_symbols(),
            self.game_field.row_fill_same_symbols(),
            self.game_field.diagonal_fill_same_symbols(),
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
        elif not self.game_field.get_empty_cells():
            self.log.append({"message": "Ничья", "color": "magenta"})
            self.status = GameStatus.GAME_OVER

    def __player_step_save(self, player: Player, step_coords: tuple) -> None:
        self.game_field.values[step_coords[1]][step_coords[0]] = player.symbol
        self.log.append(
            {
                "message": f"{player.name} поставил {player.symbol} в {step_coords}",
                "color": player.color.value,
            }
        )
        cprint(self.log[-1]["message"], self.log[-1]["color"])

    def __get_player_by_symbol(self, symbol: str) -> Player:
        for player in self.players:
            if symbol == player.symbol:
                return player

    def print_game_info(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        for record in self.log:
            cprint(record["message"], record["color"])
        for row in self.game_field.values:
            printable = "|".join([" " if cell_value is None else cell_value for cell_value in row])
            cprint(printable, "black", "on_white")

    def __get_step_coords(self, player: Player) -> tuple:
        empty_cells = self.game_field.get_empty_cells()
        if not player.is_human:
            return random.choice(empty_cells)
        return self.player_coords_input(empty_cells)

    def player_coords_input(self, empty_cells: list[tuple | None]) -> tuple[int]:
        max_range = len(self.game_field.values) - 1
        correct_input = False
        while not correct_input:
            try:
                coord_x = int(input(f"Введите координату по горизонтали (от 0 до {max_range} слева направо) "))
                coord_y = int(input(f"Введите координату по вертикали (от 0 до {max_range} сверху вниз) "))
                if empty_cells.count((coord_x, coord_y)):
                    coords = (coord_x, coord_y)
                    correct_input = True
                elif not self.game_field.is_valid_coords(coord_x, coord_y):
                    self.log.append({"message": "Координаты  ошибочны", "color": "red"})
                else:
                    self.log.append({"message": "Клетка уже занята", "color": "red"})
            except ValueError:
                self.log.append({"message": "Ошибка ввода", "color": "red"})
        return coords
