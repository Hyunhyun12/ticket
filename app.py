import json

import sentry_sdk
import yaml
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator

from config import sentry_dsn
from src.dummy_data.dummy_chair import DummyChair
from src.dummy_data.dummy_train import DummyTrain
from src.models.train import Train

app = FastAPI()

# Prometheus
Instrumentator().instrument(app).expose(app)

# CORS
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sentry
sentry_sdk.init(
    dsn=sentry_dsn,
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
    # Set profiles_sample_rate to 1.0 to profile 100%
    # of sampled transactions.
    # We recommend adjusting this value in production.
    profiles_sample_rate=1.0,
)


@app.get("/")
def read_root() -> None:
    return {"Hello": "World"}


@app.get("/dummy_train/random")
def get_dummy_train_random() -> str:
    dummy_train = DummyTrain()
    dummy_train = jsonable_encoder(dummy_train)
    dummy_train = json.dumps(dummy_train["random"])
    return dummy_train


@app.get("/dummy_train/fixed")
def get_dummy_train_fixed() -> str:
    with open("./tests/dummy_data.yaml") as file:
        dummy_train_dict = yaml.load(file, Loader=yaml.FullLoader)
    dummy_train = Train(**dummy_train_dict)
    dummy_train = jsonable_encoder(dummy_train)
    dummy_train = json.dumps(dummy_train)
    return dummy_train


@app.get("/dummy_chair/one/random")
def get_dummy_chair_random() -> str:
    dummy_chair = DummyChair().one
    dummy_chair = jsonable_encoder(dummy_chair)
    dummy_chair = json.dumps(dummy_chair[0])
    return dummy_chair

@app.get("/dummy_chair/two/random")
def get_dummy_chairs_random() -> str:
    dummy_chair = DummyChair().two
    dummy_chair = jsonable_encoder(dummy_chair)
    dummy_chair = json.dumps(dummy_chair)
    return dummy_chair

@app.get("/sample_exception")
def sample_exception() -> None:
    1 / 0
