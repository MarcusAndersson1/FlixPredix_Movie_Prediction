from fastapi import APIRouter, HTTPException
import csv

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

@router.get('/getFeatures')
def getFeatures():
    with open('./data/tmdb_5000_movies.csv','rt') as f:
        data = csv.reader(f)
    
        return next(data)

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