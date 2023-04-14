from fastapi import APIRouter, status
from fastapi.openapi.models import Response

import main
from model.Grid import Grid
from model.exceptions.GridInvalid import GridInvalid

router = APIRouter()


@router.get("/grid", status_code=status.HTTP_200_OK)
def print_grid():
    print(main.grid)
    return {main.grid.__str__()}


@router.post("/grid/{grid_dsc}", status_code=status.HTTP_200_OK)
def new_grid(grid_dsc: str):
    try:
        main.grid = Grid(grid_dsc)
    except GridInvalid as e:
        return Response(content=e.__str__(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return {str(grid_dsc)}


@router.delete("/grid", status_code=status.HTTP_200_OK)
def reset_grid():
    main.grid = Grid(None)
    return {""}
