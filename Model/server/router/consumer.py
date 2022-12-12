from fastapi import APIRouter
from pydantic import BaseModel
from enum import Enum
from typing import Set
from .. import model


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

class PredictionResponse(BaseModel):
    score: float


@router.post('/predict', response_model=PredictionResponse)
def predict(data: PredictionData):
    prediction_data = model.PredictionData(
        data.budget,
        data.runtime,
        data.genres,
        data.regions
    )

    prediction = model.predict(prediction_data)

    return {
        'score': prediction
    }


def get_router():
    return router