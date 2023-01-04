import os
import json
import joblib
import numpy as np
import pandas as pd
from . import logger
import sklearn
import sqlite3
from relationalSQLite import *

__all__ = [
    'predict',
    'load_model',
    'get_model_registry',
    'get_model_registry_location'
]

__genres = [
    'action',
    'adventure',
    'animation',
    'comedy',
    'crime',
    'documentary',
    'drama',
    'family',
    'fantasy',
    'foreign',
    'history',
    'horror',
    'music',
    'mystery',
    'romance',
    'science_fiction',
    'thriller',
    'tv_movie',
    'war',
    'western'
]

__regions = [
    'AF',
    'AS',
    'EU',
    'NA',
    'OC',
    'SA',
    'UK'
]


class PredictionData:
    def __init__(self, budget, runtime, genres, regions):
        self.budget = budget
        self.runtime = runtime
        self.genres = genres
        self.regions = regions


def predict(prediction_data: PredictionData):
    genres = __map_to_ohe(list(map(lambda x: x.value, prediction_data.genres)), __genres)
    regions = __map_to_ohe(list(map(lambda x: x.value, prediction_data.regions)), __regions)

    data_tmp = []
    data_tmp.append(prediction_data.budget)
    data_tmp.append(prediction_data.runtime)
    data_tmp.extend(genres)
    data_tmp.extend(regions)

    data = np.array([data_tmp])
    
    result = __model.predict(data)
    result = result.flatten()[0]
    return result

def retrain(df):

    X = df[['budget', 'runtime', 
        'genres_action', 'genres_adventure','genres_animation',
        'genres_comedy','genres_crime','genres_documentary',
        'genres_drama','genres_family','genres_fantasy',
        'genres_foreign','genres_history','genres_horror',
        'genres_music','genres_mystery','genres_romance',
        'genres_science_fiction','genres_thriller','genres_tv_movie',
        'genres_war','genres_western','region_AF','region_AS',
        'region_EU','region_NA','region_OC','region_SA','region_UK']].values
    y = df['vote_average'].values.reshape(-1,1)

    # copy training model
    cloned_model = sklearn.base.clone(__model)

    # partial fit on copy
    cloned_model.partial_fit(X, y)

    # compare partially fit with original / TESTING

    # Score is a bit suboptimal
    score_original = __model.score(X, y)
    score_cloned = cloned_model.score(X, y)

    if score_original > score_cloned:
        print("Model A (previous) is more accurate")
    else:
        print("Model B (new) is more accurate")
        __model = cloned_model
        

        

    

def load_model(version=-1):
    mreg = get_model_registry()
    available_models = mreg['available']

    model_entry = max(available_models, key=lambda model: model['version']) if version == -1 \
        else next((model for model in available_models if model['version'] == version), None)

    if model_entry is None:
        logger.get_logger().error("Model with version '{}' not found".format(version))
        raise Exception("Unable to load model with version '{}'".format(version))

    return joblib.load(get_model_registry_location() + '/{}.joblib'.format(model_entry['name']))

    
def get_model_registry():
    mreg_location = get_model_registry_location()

    if mreg_location is None:
        raise Exception('Unable to load model registry')

    with open(mreg_location + '/models.json') as mreg:
        return json.load(mreg)


def get_model_registry_location():
    if 'FLIXPREDIX_MREG' not in os.environ:
        logger.get_logger().error("Environment variable 'FLIXPREDIX_MREG' not set")
        return None

    return os.environ['FLIXPREDIX_MREG']


def __map_to_ohe(data, reference):
    mapping = []

    for entry in reference:
        matched = False
        for genre in data:
            if genre == entry:
                matched = True
                break

        mapping.append(1 if matched else 0)

    return mapping

__model = load_model()