class GridInvalid(Exception):

    def __init__(self, grd_description, msg):
        super().__init__("Error on model creation with descr :", grd_description, " err :", msg)