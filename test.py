import json

from fastapi.encoders import jsonable_encoder

from src.dummy_data.dummy_chair import DummyChair

dummy_chair = DummyChair()
dummy_chair = jsonable_encoder(dummy_chair)
print(json.dumps(dummy_chair))
