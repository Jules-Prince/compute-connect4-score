from fastapi import FastAPI
from api.Connect4Routes import Connect4Routes
from grid.Grid import Grid
from Score import Score

app = FastAPI()


router = Connect4Routes()
app.include_router(router.router)


if __name__ == '__main__':
    print()
    s = Score()
    grid = Grid("h00000h00000mm0000hmh000h00000h00000000000") # %6
    print(grid)
    score = s.calculate_score(grid.grdDescription)
    print(score)
