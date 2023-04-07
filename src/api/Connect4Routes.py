
from typing import Union

from fastapi import APIRouter, Response, status

from grid.Grid import Grid

class Connect4Routes():

    def __init__(self) :
        self.grid = Grid()
        self.router = APIRouter()
        self.router.add_api_route("/grid/{gridDscr}", self.newMove, status_code=status.HTTP_200_OK, methods=["POST"])
        self.router.add_api_route("/grid", self.resetGrid, status_code=status.HTTP_200_OK, methods=["DELETE"])
        self.router.add_api_route("/grid", self.printGrid, status_code=status.HTTP_200_OK, methods=["GET"])

    def printGrid(self) :
        return {self.grid.__str__()}

    def newMove(self, gridDscr: str):
        self.grid = Grid(gridDscr)
        return {str(gridDscr)}
    
    def resetGrid(self): 
        self.grid = Grid(None)
        return Response(status_code=status.HTTP_200_OK)