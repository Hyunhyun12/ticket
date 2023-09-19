from typing import List

from pydantic import BaseModel

from src.models.chair import Chair


class Car(BaseModel):
    name: int
    chairs: List[Chair]

    def __repr__(self) -> str:
        return f"\nCar\n  name={self.name}\n  chairs={self.chairs}\n"
