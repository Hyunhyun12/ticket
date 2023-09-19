from typing import List

from pydantic import BaseModel

from src.models.chair import Chair


class Car(BaseModel):
    number: int
    chairs: List[Chair]

    def __repr__(self) -> str:
        return f"\nCar\n  number={self.number}\n  chairs={self.chairs}\n"
