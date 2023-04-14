from fastapi import FastAPI
from model.Grid import Grid
from api import routers

grid = Grid()
app = FastAPI()

app.include_router(routers.router)
