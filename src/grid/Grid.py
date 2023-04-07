
import re
from grid.Case import Case
from grid.CaseNotFound import CaseNotFound
from grid.GridInvalid import GridInvalid

WIDTH  = 7
HEIGHT = 6

class Grid():


    def __init__(self, grdDescription=None): 
        print(grdDescription)
        self.grdDescription = grdDescription
        if self.grdDescription is not None:
            self.checkIfGridValid()
            columns = [self.grdDescription[i:i+HEIGHT] for i in range(0, len(self.grdDescription), HEIGHT)]
            self.cases = [Case(x, y, case) for x in range(len(columns)) for y, case in enumerate(columns[x])]
        else:
            self.cases = []

    def checkIfGridValid(self):
        if len(self.grdDescription ) > (WIDTH*HEIGHT) or len(self.grdDescription ) < (WIDTH*HEIGHT):
            raise GridInvalid(self.grdDescription , "size of the board invalid")
        if not re.match("^[0hm]*$", self.grdDescription ) :
            raise GridInvalid(self.grdDescription , "invalid value in string")
        
    def findCaseByHisCoordinates(self, x, y) :
        for case in self.cases :
            if case.x == x and case.y == y :
                return case
        
        return None

    def __str__(self) :
        string = ""
        if(len(self.cases) < WIDTH*HEIGHT) :
            return ""
        for j in range(HEIGHT-1, -1, -1) :
            for i in range(0, WIDTH,) :
                case = self.findCaseByHisCoordinates(i, j)
                if case == None :
                    raise CaseNotFound(i, j)
                string += str(case) + "\t"
            string += "\n"
        return string



