class Player:
    def __init__(self, is_human=False):
        self.name = None
        self.is_human = is_human

    def __repr__(self) -> str:
        return f"Player name: {self.name}, is_human: {self.is_human}"
