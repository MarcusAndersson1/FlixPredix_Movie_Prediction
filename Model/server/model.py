import io
import numpy as np
import pandas as pd
import sklearn
import sklearn.metrics
from . import model_registry


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


class PerformanceMetrics:
    def __init__(self, mse, r2):
        self.mse = mse
        self.r2 = r2


def predict(prediction_data: PredictionData):
    genres = __map_to_ohe(list(map(lambda x: x.value, prediction_data.genres)), __genres)
    regions = __map_to_ohe(list(map(lambda x: x.value, prediction_data.regions)), __regions)

    data_tmp = []
    data_tmp.append(prediction_data.budget)
    data_tmp.append(prediction_data.runtime)
    data_tmp.extend(genres)
    data_tmp.extend(regions)

    data = np.array([data_tmp])
    
    result = model_registry.load_active_model().predict(data)
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

    model = model_registry.load_active_model()

    # copy training model
    cloned_model = sklearn.base.clone(model)

    # partial fit on copy
    cloned_model.partial_fit(X, y)

    # compare partially fit with original / TESTING

    # Score is a bit suboptimal
    score_original = model.score(X, y)
    score_cloned = cloned_model.score(X, y)

    if score_original > score_cloned:
        print("Model A (previous) is more accurate")
    else:
        print("Model B (new) is more accurate")
        model = cloned_model ## TODO


def get_performance_metrics(dataset):
    content = io.StringIO(dataset.read().decode("utf-8"))

    df = pd.read_csv(content, sep=',')
    
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
    
    model = model_registry.load_active_model()
    prediction = model.predict(X)

    mse = sklearn.metrics.mean_squared_error(y, prediction)
    r2 = model.score(X, y)

    return PerformanceMetrics(mse, r2)


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