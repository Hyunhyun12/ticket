from pydantic import BaseModel


class Chair(BaseModel):
    name: str
    is_reservated: bool
    is_used: bool

    def __repr__(self) -> str:
        return f"\nChair\n  name={self.name}\n  is_reservated={self.is_reservated}\n  is_used={self.is_used}\n"
