from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from enum import Enum
from typing import Set


__all__ = [
    'get_router'
]


router = APIRouter(
    prefix='/consumer'
)

class Genre(Enum):
    action = 'action'
    adventure = 'adventure'
    animation = 'animation'
    comedy = 'comedy'
    crime = 'crime'
    documentary = 'documentary'
    drama = 'drama'
    family = 'family'
    fantasy = 'fantasy'
    foreign = 'foreign'
    history = 'history'
    horror = 'horror'
    music = 'music'
    mystery = 'mystery'
    romance = 'romance'
    science_fiction = 'science_fiction'
    thriller = 'thriller'
    tv_movie = 'tv_movie'
    war = 'war'
    western = 'western'

class Region(Enum):
    africa = 'AF'
    asia = 'AS'
    europe = 'EU'
    north_america = 'NA'
    oceania = 'OC'
    south_america = 'SA'
    united_kingdom = 'UK'

class PredictionData(BaseModel):
    budget: int
    runtime: int
    genres: Set[Genre]
    regions: Set[Region]


@router.post('/predict')
def predict(prediction_data: PredictionData):
    raise HTTPException(status_code=501, detail='Not implemented')


def get_router():
    return router