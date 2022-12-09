from fastapi import FastAPI
from .router import admin, consumer


app = FastAPI()

app.include_router(admin.get_router())
app.include_router(consumer.get_router())