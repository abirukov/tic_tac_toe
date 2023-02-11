import os

from termcolor import cprint

import config
import numpy
import random
from player import Player


class Game:
    def __init__(self):
        self.game_field = [[None for _ in range(config.GAME_FIELD_SIZE)] for _ in range(config.GAME_FIELD_SIZE)]
        self.log = []
        self.players = []
        self.status = "in_process"

    def add_player(self, player: Player) -> None:
        self.players.append(player)

    def change_step_order(self) -> None:
        for _ in range(random.randint(0, 20)):
            random.shuffle(self.players)

    def set_symbols(self) -> None:
        for i, player in enumerate(self.players):
            player.symbol = config.SYMBOLS[i]

    def set_colors(self) -> None:
        for i, player in enumerate(self.players):
            player.color = config.COLORS[i]

    def step(self) -> None:
        for player in self.players:
            if self.status == "in_process":
                empty_cells = self.__get_empty_cells()
                player_step_coords = player.get_step_coords(empty_cells)
                self.__player_step_save(player, player_step_coords)
                self.__check_game_status()
                self.print_game_info()

    def __get_empty_cells(self) -> list[tuple | None]:
        empty_cells = []
        for y, row in enumerate(self.game_field):
            for x, value in enumerate(row):
                if value is None:
                    empty_cells.append((x, y))
        return empty_cells

    def __check_game_status(self):
        winner_symbol = None
        check_winner_results = [
            self.__column_fill_same_symbols(),
            self.__row_fill_same_symbols(),
            self.__diagonal_fill_same_symbols(),
        ]
        for result in check_winner_results:
            if result is not None:
                winner_symbol = result

        if winner_symbol:
            winner = self.__get_player_by_symbol(winner_symbol)
            if winner is not None:
                self.log.append({"message": f"Победил {winner.name}", "color": "magenta"})
            else:
                self.log.append({"message": "Не нашли победителя, обратитесь к разработчику", "color": "magenta"})
            self.status = "game_over"
        elif len(self.__get_empty_cells()) == 0:
            self.log.append({"message": "Ничья", "color": "magenta"})
            self.status = "game_over"

    def __player_step_save(self, player: Player, step_coords: tuple) -> None:
        self.game_field[step_coords[1]][step_coords[0]] = player.symbol
        self.log.append({"message": f"{player.name} поставил {player.symbol} в {step_coords}", "color": player.color})
        cprint(self.log[-1]["message"], self.log[-1]["color"])

    def __column_fill_same_symbols(self) -> None | str:
        result = None
        for i in range(config.GAME_FIELD_SIZE):
            column = [row[i] for row in self.game_field]
            if column.count(column[0]) == len(column):
                result = column[0]
        return result

    def __row_fill_same_symbols(self) -> None | str:
        result = None
        for row in self.game_field:
            if row.count(row[0]) == len(row):
                result = row[0]
        return result

    def __diagonal_fill_same_symbols(self) -> None | str:
        result = None
        matrix = numpy.array(self.game_field)
        left_diagonal = matrix.diagonal().tolist()
        if left_diagonal.count(left_diagonal[0]) == len(left_diagonal):
            result = left_diagonal[0]
        right_diagonal = numpy.fliplr(matrix).diagonal().tolist()
        if right_diagonal.count(right_diagonal[0]) == len(right_diagonal):
            result = right_diagonal[0]
        return result

    def __get_player_by_symbol(self, symbol: str) -> Player | None:
        for player in self.players:
            if player.symbol == symbol:
                return player
        return None

    def print_game_info(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")
        for record in self.log:
            cprint(record["message"], record["color"])
        for row in self.game_field:
            printable = "|".join([" " if x is None else x for x in row])
            cprint(printable, "black", "on_white")
