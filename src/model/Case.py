import emoji
from src.model.Piece import Piece


class Case:
    def __init__(self, x, y, piece):
        self.x = x
        self.y = y
        self.piece = piece

    def __str__(self):
        if self.piece.value == Piece.MACHINE.value:
            return emoji.emojize(":yellow_square:")
        elif self.piece.value == Piece.HUMAN.value:
            return emoji.emojize(":red_square:")
        else:
            return emoji.emojize(":white_large_square:")
