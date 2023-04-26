from pydantic import BaseModel


class Move_DTO(BaseModel):
    column: int
