import os
import time
import sqlite3


MODEL_REGISTRY_LOCATION = "models/models.db"
MODEL_LOCATION = "models/tmp/model.joblib"


def insert_model(name, version, created_at):
    try:
        connection = sqlite3.connect(MODEL_REGISTRY_LOCATION)
        cursor = connection.cursor()

        query = """INSERT INTO models
                            (name, version, created_at) VALUES (?, ?, ?)"""

        columns = (name, version, created_at)

        cursor.execute(query, columns)
        connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print('Error occured while inserting model', error)

    finally:
        if connection:
            connection.close()


def get_new_version():
    try:
        connection = sqlite3.connect(MODEL_REGISTRY_LOCATION)
        cursor = connection.cursor()

        query = 'SELECT MAX(version) FROM models LIMIT 1'
        cursor.execute(query)

        version = cursor.fetchone()

        if version[0] is None:
            return 1

        return version[0] + 1
    except sqlite3.Error as error:
        print('Error occured while fetching latest version', error)
    finally:
        if connection:
            connection.close()


model_version = get_new_version()
model_name = 'model-v{}'.format(model_version)
model_created_at = int(time.time())

insert_model(model_name, model_version, model_created_at)

os.rename(MODEL_LOCATION, "models/{}.joblib".format(model_name))
