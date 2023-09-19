import json

import yaml
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

from src.dummy_data.dummy_train import DummyTrain
from src.models.train import Train

app = FastAPI()


@app.get("/")
def read_root() -> None:
    return {"Hello": "World"}


@app.get("/dummy_data/random")
def get_dummy_data_random() -> str:
    dummy_train = DummyTrain()
    dummy_train = jsonable_encoder(dummy_train)
    dummy_train = json.dumps(dummy_train["random"])
    return dummy_train


@app.get("/dummy_data/fixed")
def get_dummy_data_fixed() -> str:
    with open("./tests/dummy_data.yaml") as file:
        dummy_train_dict = yaml.load(file, Loader=yaml.FullLoader)
    dummy_train = Train(**dummy_train_dict)
    dummy_train = jsonable_encoder(dummy_train)
    dummy_train = json.dumps(dummy_train)
    return dummy_train
