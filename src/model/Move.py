from src.model.Piece import Piece


class Move:

    def __init__(self, column, player: Piece):
        self.column = column
        self.player = player