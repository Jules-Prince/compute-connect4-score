from enum import Enum


class Piece(Enum):
    HUMAN = 'h'
    MACHINE = 'm'
    BLANK = '0'

    def __new__(cls, value):
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

