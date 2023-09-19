from pydantic import BaseModel


class Chair(BaseModel):
    number: int
    is_reservated: bool
    is_used: bool
