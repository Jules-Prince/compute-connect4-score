from fastapi import FastAPI
from api.Connect4Routes import Connect4Routes
from grid.Grid import Grid

app = FastAPI()

router = Connect4Routes()
app.include_router(router.router)
