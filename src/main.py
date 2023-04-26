from fastapi import FastAPI
from src.model.Grid import Grid
from src.api import routers
from src.MinMax import MinMax

grid = Grid("000000000000000000000000000000000000000000")
app = FastAPI()
min_max = MinMax()

app.include_router(routers.router)
