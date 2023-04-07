
class GridInvalid(Exception) :
    
    def __init__(self, grdDescription, msg) :
        super().__init__("Error on grid creation with descr :", grdDescription, " err :", msg)