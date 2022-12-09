from fastapi import APIRouter, HTTPException

__all__ = [
    'get_router'
]


router = APIRouter(
    prefix='/admin'
)


@router.post('/train')
def train():
    raise HTTPException(status_code=501, detail='Not implemented')


@router.post('/validate')
def validate():
    raise HTTPException(status_code=501, detail='Not implemented')


@router.post('/activate')
def activate():
    raise HTTPException(status_code=501, detail='Not implemented')


def get_router():
    return router