from fastapi import APIRouter, status, Request
from fastapi.openapi.models import Response


from src import main
from src.MinMax import MinMax
from src.Score import Score
from src.model.Grid import Grid
from src.model.Move import Move
from src.model.Piece import Piece
from src.api.model_dto.Move_DTO import Move_DTO
from src.model.exceptions.GridInvalid import GridInvalid

router = APIRouter()

title = """
██████  ██    ██ ██ ███████ ███████  █████  ███    ██  ██████ ███████     ██   ██ 
██   ██ ██    ██ ██ ██      ██      ██   ██ ████   ██ ██      ██          ██   ██ 
██████  ██    ██ ██ ███████ ███████ ███████ ██ ██  ██ ██      █████       ███████ 
██      ██    ██ ██      ██      ██ ██   ██ ██  ██ ██ ██      ██               ██ 
██       ██████  ██ ███████ ███████ ██   ██ ██   ████  ██████ ███████          ██ 
"""
print(title)

@router.post("/grid/new_grid/{grid_dsc}", status_code=status.HTTP_200_OK)
def new_grid(grid_dsc: str):
    print("wtf")
    try:
        main.grid = Grid(grid_dsc)
    except GridInvalid as e:
        return Response(content=e.__str__(), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return {str(grid_dsc)}

@router.post("/grid/new_move/{move_dto}", status_code=status.HTTP_200_OK)
def new_move(move_dto: str):
    print("\n##################################################")
    print("NOUVEAU TOUR")
    print("##################################################\n")
    end = False
    move_dto = int(move_dto)
    
    if move_dto > 6 or move_dto < 0:
        print("ERROR : BAD COLUMN VALUE ... ARG <= 6 AND ARG >= 0")
    else :
        try:
            score = Score()
            move = Move(move_dto, Piece.HUMAN)
            main.grid.play_move(move)
            print("\nJoueur : ")
            print_grid()
            sc = score.calculate_score(main.grid, Piece.HUMAN)
            print("HUMAIN SCORE : ", sc) 
            if score.calculate_score(main.grid, Piece.HUMAN) >= 1000:
                print("\n!!!!!!!!! HUMAIN WIN !!!!!!!!!\n")
                end = True
            if end:    
                reset_grid()
                end = False
            else:
                main.min_max = MinMax()
                opponent_move = main.min_max.get_best_move(main.grid, Piece.MACHINE)
                main.grid.play_move(opponent_move)
                print("\nMachine : ")
                print_grid()
                sc = score.calculate_score(main.grid, Piece.MACHINE)
                print("MACHINE SCORE : ", sc) 
                if sc >= 1000:
                    print("\n!!!!!!!!! MACHINE WIN !!!!!!!!!\n")  
                    reset_grid()       
            
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