import re
from src.model.Case import Case
from src.model.exceptions.CaseNotFound import CaseNotFound
from src.model.exceptions.GridInvalid import GridInvalid
from src.model.Piece import Piece

WIDTH = 7
HEIGHT = 6


class Grid:
    def __init__(self, grd_description: str = None, cases: list[Case] = None):
        self.cases = cases
        #print(grd_description)
        self.grd_description = grd_description
        if self.grd_description is not None:
            if self.cases is None:
                self.check_if_grid_valid()
                columns = [self.grd_description[i:i + HEIGHT] for i in range(0, len(self.grd_description), HEIGHT)]
                self.cases = [Case(x, y, Piece(piece)) for x in range(len(columns)) for y, piece in enumerate(columns[x])]
        else:
            self.cases = []

    def play_move(self, move):
        column = self.get_column(move.column)
        filtered_cases = list(filter(lambda case: case.piece.value == Piece.BLANK.value, column))
        case_to_put_piece = min(filtered_cases, key=lambda case: case.y)
        case_to_put_piece.piece = move.player



    def check_if_grid_valid(self):
        if len(self.grd_description) > (WIDTH * HEIGHT) or len(self.grd_description) < (WIDTH * HEIGHT):
            raise GridInvalid(self.grd_description, "size of the board invalid")
        if not re.match("^[0hm]*$", self.grd_description):
            raise GridInvalid(self.grd_description, "invalid value in string")

    def get_case_at(self, x, y) -> Case:
        for case in self.cases:
            if case.x == x and case.y == y:
                return case

        return None

    def get_column(self, nb_column):
        column = []
        for case in self.cases:
            if case.x == nb_column:
                column.append(case)
        return column

    def get_all_cases_different(self, other_grid):
        other_cases = other_grid.cases
        return list(filter(lambda case1: all(case1.x != case2.x or case1.y != case2.y or case1.piece.value != case2.piece.value for case2 in self.cases), other_cases))


    def __str__(self):
        string = ""
        if len(self.cases) < WIDTH * HEIGHT:
            return ""
        for j in range(HEIGHT - 1, -1, -1):
            for i in range(0, WIDTH):
                case = self.get_case_at(i, j)
                if case is None:
                    raise CaseNotFound(i, j)
                string += str(case) + "\t"
            string += "\n"
        return string
