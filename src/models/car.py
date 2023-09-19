from typing import List

from pydantic import BaseModel

from src.models.chair import Chair


class Car(BaseModel):
    name: str
    chairs: List[Chair]
