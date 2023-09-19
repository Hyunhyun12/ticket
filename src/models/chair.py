from pydantic import BaseModel


class Chair(BaseModel):
    number: str
    is_reservated: bool
    is_used: bool

    def __repr__(self) -> str:
        return f"\nChair\n  number={self.number}\n  is_reservated={self.is_reservated}\n  is_used={self.is_used}\n"
