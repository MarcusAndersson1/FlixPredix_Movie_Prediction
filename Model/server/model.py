import os
import json
import joblib
from . import logger

__all__ = [
    'predict',
    'load_model',
    'get_model_registry',
    'get_model_registry_location'
]


def predict(data):
    pass


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


__model = load_model()