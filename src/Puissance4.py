from fastapi import FastAPI
# from api.Connect4Routes import Connect4Routes
from model.Grid import Grid
from Score import Score
from MinMax import MinMax
from model.Move import Move
from model.Piece import Piece

app = FastAPI()

# router = Connect4Routes()
# app.include_router(router.router)


if __name__ == '__main__':
    print()

    s = Score()
    grid = Grid("000000000000000000000000000000000000000000")  # %6
    print(grid)

    player = Piece.HUMAN
    score = s.calculate_score(grid, player)
    print("Score de ", player.value, ": ", score)

    player = Piece.MACHINE
    score = s.calculate_score(grid, player)
    print("Score de ", player.value, ": ", score)

    min_max = MinMax()
    for i in range(4):
        grid.play_move(Move(1, Piece.HUMAN))
        print(grid)
        best_move = min_max.get_best_move(grid, Piece.MACHINE)
        grid.play_move(best_move)
        print(grid)

