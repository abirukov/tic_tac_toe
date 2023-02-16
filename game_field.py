class GameField:
    def __init__(self, field_size: int):
        self.values = [[None for _ in range(field_size)] for _ in range(field_size)]

    def get_empty_cells(self) -> list[tuple | None]:
        empty_cells = []
        for row_index, row in enumerate(self.values):
            for column_index, value in enumerate(row):
                if value is None:
                    empty_cells.append((column_index, row_index))
        return empty_cells

    def column_fill_same_symbols(self) -> str | None:
        result = None
        for column_index in range(len(self.values)):
            column = [row[column_index] for row in self.values]
            if column.count(column[0]) == len(column):
                result = column[0]
        return result

    def row_fill_same_symbols(self) -> str | None:
        result = None
        for row in self.values:
            if row.count(row[0]) == len(row):
                result = row[0]
        return result

    def diagonal_fill_same_symbols(self) -> str | None:
        result = None
        left_diagonal = self.__get_diagonal_values()
        if left_diagonal.count(left_diagonal[0]) == len(left_diagonal):
            result = left_diagonal[0]
        right_diagonal = self.__get_diagonal_values(reverse=True)
        if right_diagonal.count(right_diagonal[0]) == len(right_diagonal):
            result = right_diagonal[0]
        return result

    def __get_diagonal_values(self, reverse=False) -> list:
        diagonal_values = []
        for row_index, row in enumerate(self.values):
            if reverse:
                needle_column_position = len(row) - 1 - row_index
            else:
                needle_column_position = row_index
            diagonal_values.append(self.values[row_index][needle_column_position])
        return diagonal_values

    def is_valid_coords(self, coord_x: int, coord_y: int) -> bool:
        return 0 <= coord_x < len(self.values[0]) and 0 <= coord_y < len(self.values)
