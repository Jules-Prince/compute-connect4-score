import emoji


class Case:
    def __init__(self, x, y, piece):
        self.x = x
        self.y = y
        self.piece = piece

    def __str__(self):
        p = ""
        if self.piece == 'm':
            p = emoji.emojize(":yellow_square:")
        elif self.piece == 'h':
            p = emoji.emojize(":red_square:")
        elif self.piece == 'x':
            p = emoji.emojize(":green_square:")
        else:
            p = emoji.emojize(":white_large_square:")
        return p