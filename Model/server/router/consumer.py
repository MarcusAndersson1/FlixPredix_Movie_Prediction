from fastapi import APIRouter, HTTPException

__all__ = [
    'get_router'
]


router = APIRouter(
    prefix='/consumer'
)


@router.post('/predict')
def predict():
    raise HTTPException(status_code=501, detail='Not implemented')


def get_router():
    return router