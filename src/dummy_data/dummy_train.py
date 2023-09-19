import random
from typing import Generator, List

from src.models.car import Car
from src.models.chair import Chair
from src.models.train import Train


class DummyTrain:
    def __init__(self) -> None:
        self.dummy_train = self.get_dummy_train()

    def get_dummy_train(self) -> Train:
        cars = self.get_dummy_cars()
        return Train(
            name="KTX",
            number=37,
            cars=cars,
        )

    def get_dummy_cars(self) -> List[Car]:
        chairs = self.get_random_chair()
        return [
            Car(
                number=9,
                chairs=chairs,
            )
        ]

    def get_random_chair(self) -> List[Chair]:
        chair_name_generator = self.chair_name_generator()
        return [
            Chair(
                name=chair_name,
                is_reservated=random.choice((True, False)),
                is_used=random.choice((True, False)),
            )
            for chair_name in chair_name_generator
        ]

    def chair_name_generator(self) -> Generator[None, None, str]:
        for number in range(1, 16):
            for alphabet in ["A", "B", "C", "D"]:
                yield f"{number}{alphabet}"
