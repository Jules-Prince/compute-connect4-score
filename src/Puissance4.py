from fastapi import FastAPI
#from api.Connect4Routes import Connect4Routes
from grid.Grid import Grid
from Score import Score
from MinMax import MinMax

app = FastAPI()


#router = Connect4Routes()
#app.include_router(router.router)


if __name__ == '__main__':
    print()
    
    s = Score()
    grid = Grid("h00000hm0000mm0000hmh000hh0000h00000000000") # %6
    print(grid)
    
    player = 'h'
    score = s.calculate_score(grid.grdDescription, player)
    print("Score de ",player,": ", score)
    
    player = 'm'
    score = s.calculate_score(grid.grdDescription, player)
    print("Score de ",player,": ", score)
    
    
    min_max =  MinMax()
    min_max.get_best_move(grid.convert(), 'h')