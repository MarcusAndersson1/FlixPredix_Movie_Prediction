import os
import json
import time

MODEL_REGISTRY_LOCATION = "models/models.json"
MODEL_LOCATION = "models/tmp/model.joblib"

if not os.path.exists(MODEL_LOCATION):
    exit(-1)

registy_content = None

with open(MODEL_REGISTRY_LOCATION) as model_registry:
    registry_content = json.load(model_registry)

    available_models: list = registry_content['available']

    if len(available_models) == 0:
        model_version = 1
    else:
        model_version = max(list(map(lambda x: x['version'], available_models))) + 1

    model_name = 'model-v{}'.format(model_version)
    model_created_at = int(time.time())

    model_entry = {
        'name': model_name,
        'version': model_version,
        'createdAt': model_created_at
    }

    available_models.append(model_entry)

    os.rename(MODEL_LOCATION, "models/{}.joblib".format(model_name))
    

if registry_content is None:
    exit(-1)

with open(MODEL_REGISTRY_LOCATION, 'w') as model_registry:
    model_registry.write(json.dumps(registry_content, indent=4))
