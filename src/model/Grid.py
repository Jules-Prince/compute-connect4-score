import re
from model.Case import Case
from model.exceptions.CaseNotFound import CaseNotFound
from model.exceptions.GridInvalid import GridInvalid

WIDTH = 7
HEIGHT = 6


class Grid:
    def __init__(self, grd_description: str = None, cases: list[Case] = None):
        self.cases = cases
        print(grd_description)
        self.grd_description = grd_description
        if self.grd_description is not None:
            if self.cases is None:
                self.check_if_grid_valid()
                columns = [self.grd_description[i:i + HEIGHT] for i in range(0, len(self.grd_description), HEIGHT)]
                self.cases = [Case(x, y, case) for x in range(len(columns)) for y, case in enumerate(columns[x])]
        else:
            self.cases = []

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

    def __str__(self):
        string = ""
        if len(self.cases) < WIDTH * HEIGHT:
            return ""
        for j in range(HEIGHT - 1, -1, -1):
            for i in range(0, WIDTH, ):
                case = self.get_case_at(i, j)
                if case is None:
                    raise CaseNotFound(i, j)
                string += str(case) + "\t"
            string += "\n"
        return string
