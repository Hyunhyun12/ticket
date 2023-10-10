import random
from typing import List

from src.models.chair import Chair


class DummyChair:
    def __init__(self) -> None:
        self.random = self.get_random_chair()

    def get_random_chair(self) -> List[Chair]:
        return [
            Chair(
                name="1A",
                is_reservated=random.choice((True, False)),
                is_used=random.choice((True, False)),
            )
        ]
