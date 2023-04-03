
from grid.Case import Case
from grid.CaseNotFound import CaseNotFound

WIDTH  = 7
HEIGHT = 6

class Grid():

    def __init__(self, brdDescription): 
        columns = [brdDescription[i:i+HEIGHT] for i in range(0, len(brdDescription), HEIGHT)]

        self.cases = [Case(x, y, case) for x in range(len(columns)) for y, case in enumerate(columns[x])]


    def findCaseByHisCoordinates(self, x, y) :
        for case in self.cases :
            if case.x == x and case.y == y :
                return case
        
        return None

    def __str__(self) :
        string = ""
        for j in range(HEIGHT-1, -1, -1) :
            for i in range(0, WIDTH,) :
                case = self.findCaseByHisCoordinates(i, j)
                if case == None :
                    raise CaseNotFound(i, j)
                string += str(case) + "\t"
            string += "\n"
        return string



