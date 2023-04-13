from fastapi import FastAPI
from api.Connect4Routes import Connect4Routes
from grid.Grid import Grid
from score import Score

<<<<<<< HEAD
app = FastAPI()
=======
def main():
    s = Score()
    grid = Grid("h00000h00000mm0000hmh000h00000h00000000000") # %6
    print(grid)
    grid = s.run(grid)
    #print(grid)
>>>>>>> ea50c0e (score)

router = Connect4Routes()
app.include_router(router.router)
