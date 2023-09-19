from typing import List

from pydantic import BaseModel

from src.models.chair import Chair


class Car(BaseModel):
    chairs: List[Chair]
