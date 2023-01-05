from .. import model_registry
from typing import List
from fastapi import APIRouter, HTTPException, UploadFile
from pydantic import BaseModel
import csv

__all__ = [
    'get_router'
]


router = APIRouter(
    prefix='/admin'
)


class ActivateData(BaseModel):
    version: int


class ActivateResponse(BaseModel):
    version: int


class ModelResponse(BaseModel):
    name: str
    version: int
    active: bool

class ListModelResponse(BaseModel):
    models: List[ModelResponse]


@router.post('/train')
def train():
    raise HTTPException(status_code=501, detail='Not implemented')


@router.post('/validate')
def validate():
    raise HTTPException(status_code=501, detail='Not implemented')


@router.post('/upload')
def upload(file: UploadFile):
    model_registry.persist_model(file.file)


@router.post('/activate')
def activate(data: ActivateData):
    if data.version < 0:
        raise HTTPException(status_code=400, detail="Invalid version value: '{}'".format(data.version))

    try:
        model_registry.set_active_model(data.version)
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to set version '{}' as active model".format(data.version))


@router.get('/models', response_model=ListModelResponse)
def models():
    models = model_registry.get_models()
    active_model = model_registry.get_active_model()

    return {
        'models': list(map(lambda model: {'name': model.name, 'version': model.version, 'active': model.version == active_model.version}, models))
    }

@router.get('/getGenres')
def getFeatures():
    with open('./data/tmdb_5000_movies.csv','rt') as f:
        data = csv.reader(f)

        genres = []
        values = []

        for row in data:
            try:
                temp = row[1].split(":")
                temp = temp[2].split("}")
                temp = temp[0][2:-1]
                # print(temp)
                res = genres.index(temp)
                values[res] += 1
            except:
                if(len(temp) > 1):
                    genres.append(temp)
                    values.append(1)
                
    return genres + values

@router.get('/getAvgBudget')
def getFeatures():
    with open('./data/tmdb_5000_movies.csv','rt') as f:
        data = csv.reader(f)
        next(data)
        
        budget = 0
        len = 0
        for row in data:
            if(row[0] != 0):
                budget += int(row[0])
                len+=1
        
        return budget/len


def get_router():
    return router