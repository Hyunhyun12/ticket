import json

from fastapi.encoders import jsonable_encoder

from src.dummy_data.dummy_train import DummyTrain

dummy_train = DummyTrain().dummy_train
dummy_train = jsonable_encoder(dummy_train)
print(json.dumps(dummy_train))
