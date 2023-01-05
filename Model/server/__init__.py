from . import model_registry
from .router import admin, consumer
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

if model_registry.get_model_registry_location() is None:
    exit(-1)

app = FastAPI()

@app.get('/', status_code=200)
def ping():
    return {}

app.include_router(admin.get_router())
app.include_router(consumer.get_router())

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=["*"],
    allow_headers=["*"]
)