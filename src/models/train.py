from typing import List

from pydantic import BaseModel

from src.models.car import Car


class Train(BaseModel):
    name: str
    chairs: List[Car]
