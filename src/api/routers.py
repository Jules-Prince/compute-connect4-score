from fastapi import APIRouter, status, Request
from fastapi.openapi.models import Response


import main
from MinMax import MinMax
from model.Grid import Grid
from model.Move import Move
from model.Piece import Piece
from api.model_dto.Move_DTO import Move_DTO
from model.exceptions.GridInvalid import GridInvalid

router = APIRouter()

@router.post("/grid/new_grid/{grid_dsc}", status_code=status.HTTP_200_OK)
def new_grid(grid_dsc: str):
    print("wtf")
    try:
        main.grid = Grid(grid_dsc)
    except GridInvalid as e:
        return Response(content=e.__str__(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return {str(grid_dsc)}


@router.post("/grid/new_move", status_code=status.HTTP_200_OK)
def new_move(move_dto: Move_DTO):
    try:
        move = Move(move_dto.column, Piece.HUMAN)
        main.grid.play_move(move)
        main.min_max = MinMax()
        opponent_move = main.min_max.get_best_move(main.grid, Piece.MACHINE)
        main.grid.play_move(opponent_move)
        print_grid()
    except Exception as e:
        return Response(content="Invalid request body", status_code=status.HTTP_400_BAD_REQUEST)


@router.get("/grid", status_code=status.HTTP_200_OK)
def print_grid():
    print(main.grid)
    return {main.grid.__str__()}


@router.delete("/grid", status_code=status.HTTP_200_OK)
def reset_grid():
    main.grid = Grid("000000000000000000000000000000000000000000")
    return {""}
