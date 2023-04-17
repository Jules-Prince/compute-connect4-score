from fastapi import FastAPI
from model.Grid import Grid
from api import routers
from MinMax import MinMax

grid = Grid("000000000000000000000000000000000000000000")
app = FastAPI()
min_max = MinMax()

app.include_router(routers.router)
