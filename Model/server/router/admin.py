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