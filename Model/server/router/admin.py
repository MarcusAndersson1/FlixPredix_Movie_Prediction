from fastapi import APIRouter, HTTPException, UploadFile
from pydantic import BaseModel
from enum import Enum
from typing import Set
from .. import model
from .. import scripts
import csv
import pandas as pd
from model import retrain
from relationalSQLite import *

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
    retrain(df)
    



@router.post('/validate')
def validate():
    raise HTTPException(status_code=501, detail='Not implemented')
    # send in csv file
    # check score


@router.post('/activate')
def activate():
    raise HTTPException(status_code=501, detail='Not implemented')

@router.get('/models')
def models():
    return {
        getModels()
    }
    



def get_router():
    return router