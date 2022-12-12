from . import model
from fastapi import FastAPI
from .router import admin, consumer

if model.get_model_registry_location() is None:
    exit(-1)

app = FastAPI()

app.include_router(admin.get_router())
app.include_router(consumer.get_router())