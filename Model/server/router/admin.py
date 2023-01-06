from .. import model_registry, model
from typing import List
from fastapi import APIRouter, HTTPException, UploadFile
from pydantic import BaseModel

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


class ValidationResponse(BaseModel):
    mse: float
    r2: float


class ModelResponse(BaseModel):
    name: str
    version: int
    active: bool

class ListModelResponse(BaseModel):
    models: List[ModelResponse]


@router.post('/train')
def train():
    raise HTTPException(status_code=501, detail='Not implemented')


@router.post('/validate', response_model=ValidationResponse)
def validate(file: UploadFile):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Supported file types: ['{}']".format('csv'))

    performance_metrics = model.get_performance_metrics(file.file)

    return {
        'mse': performance_metrics.mse,
        'r2': performance_metrics.r2
    }


@router.post('/upload')
def upload(file: UploadFile):
    if not file.filename.endswith('.joblib'):
        raise HTTPException(status_code=400, detail="Supported file types: ['{}']".format('joblib'))

    model_registry.persist_model(file.file)


@router.post('/activate', response_model=ActivateResponse)
def activate(data: ActivateData):
    if data.version < 0:
        raise HTTPException(status_code=400, detail="Invalid version value: '{}'".format(data.version))

    try:
        model_registry.set_active_model(data.version)

        return {
            'version': model_registry.get_active_model().version
        }
    except Exception:
        raise HTTPException(status_code=400, detail="Failed to set version '{}' as active model".format(data.version))


@router.get('/models', response_model=ListModelResponse)
def models():
    models = model_registry.get_models()
    active_model = model_registry.get_active_model()

    return {
        'models': list(map(lambda model: {'name': model.name, 'version': model.version, 'active': model.version == active_model.version}, models))
    }


def get_router():
    return router