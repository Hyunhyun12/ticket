from typing import List

from pydantic import BaseModel

from src.models.car import Car


class Train(BaseModel):
    name: str
    number: int
    cars: List[Car]

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return (
            f"Train\n  name={self.name}\n  number={self.number}\n  cars={self.cars}\n"
        )
