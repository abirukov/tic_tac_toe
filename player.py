from game_enums import Color


class Player:
    def __init__(self, symbol: str, color: Color, is_human=False):
        self.name = None
        self.is_human = is_human
        self.symbol = symbol
        self.color = color

    def __repr__(self) -> str:
        return f"Player name: {self.name}, is_human: {self.is_human}, symbol: {self.symbol}, color: {self.color}"
