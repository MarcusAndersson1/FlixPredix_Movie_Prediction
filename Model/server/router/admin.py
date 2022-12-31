from fastapi import APIRouter, HTTPException, UploadFile
from pydantic import BaseModel
from enum import Enum
from typing import Set
from .. import model
from .. import scripts
import csv
import pandas as pd


__all__ = [
    'get_router'
]


router = APIRouter(
    prefix='/admin'
)


@router.post('/train')

async def upload_csv(file: UploadFile):

    # Check if the file is a CSV file
    if not file.filename.endswith('.csv'):
        return 'Invalid file', 400

    # Read the CSV file
    result = csv.reader(file.file)

    # Return the result to the client
    return result
    
def train_with_csv(csv_file):

    # step 1: convert CSV into a pandas dataframe
    df = pd.read_csv(csv_file, sep=',')

    # step 2: retrain model with new dataframe DONE
  

    # step 3: test model
    

    # step 4: save and replace model as active if performs better
    # create SQLite database?
    



@router.post('/validate')
def validate():
    raise HTTPException(status_code=501, detail='Not implemented')
    # send in csv file
    # check score


@router.post('/activate')
def activate():
    raise HTTPException(status_code=501, detail='Not implemented')


def get_router():
    return router