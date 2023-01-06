from . import logger
import os
import sqlite3
import joblib
import time


class Model:
    def __init__(self, name: str, version: int, created_at: int):
        self.name = name
        self.version = version
        self.created_at = created_at


def create_model(name, version, created_at):
    try:
        connection = sqlite3.connect(get_model_registry_location() + '/models.db')
        cursor = connection.cursor()

        query = '''INSERT INTO models
                            (name, version, created_at) VALUES (?, ?)'''

        cursor.execute(query, (name, version, created_at))
        connection.commit()

        cursor.close()
    except sqlite3.Error as error:
        logger.get_logger().error('Error occured while inserting model')
        logger.get_logger().error(error)
    finally:
        if connection:
            connection.close()


def get_model_by_version(version):
    try:
        connection = sqlite3.connect(get_model_registry_location() + '/models.db')
        cursor = connection.cursor()

        query = 'SELECT name, version, created_at FROM models WHERE version=? LIMIT 1'
        cursor.execute(query, (version,))

        model = cursor.fetchone()

        cursor.close()
        
        if model is None:
            logger.get_logger().error("Failed to find model with version '%d'", version)
            return None
        
        return Model(model[0], model[1], model[2])
    except sqlite3.Error as error:
        logger.get_logger().error("Error occurred while fetching model with version '%d'", version)
        logger.get_logger().error(error)
    finally:
        if connection:
            connection.close()


def get_active_model():
    try:
        connection = sqlite3.connect(get_model_registry_location() + '/models.db')
        cursor = connection.cursor()

        query = '''SELECT models.name, models.version, models.created_at FROM models
                    JOIN active ON active.active = models.version LIMIT 1'''

        cursor.execute(query)

        model = cursor.fetchone()

        cursor.close()

        if model is None:
            logger.get_logger().error('Failed to fetch active model')
            raise Exception('Failed to fetch active model')


        return Model(model[0], model[1], model[2])
    except sqlite3.Error as error:
        logger.get_logger().error("Error occurred while fetching active model")
        logger.get_logger().error(error)
    finally:
        if connection:
            connection.close()


def set_active_model(version):
    try:
        model = get_model_by_version(version)
        
        if model is None:
            raise Exception("Failed to find model with version '%d'", version)

        connection = sqlite3.connect(get_model_registry_location() + '/models.db')
        cursor = connection.cursor()

        query = 'UPDATE active SET active = ?'

        cursor.execute(query, (version,))
        connection.commit()

        cursor.close()
    except sqlite3.Error as error:
        logger.get_logger().error("Error occurred while setting active model")
        logger.get_logger().error(error)
    finally:
        if connection:
            connection.close()


def get_models():
    try:
        connection = sqlite3.connect(get_model_registry_location() + '/models.db')
        cursor = connection.cursor()
        
        query = 'SELECT name, version, created_at from models'

        cursor.execute(query)
        models = cursor.fetchall()

        cursor.close()

        return list(map(lambda model: Model(model[0], model[1], model[2]), models))
    except sqlite3.Error as error:
        logger.get_logger().error('Error occured while fetching models')
        logger.get_logger().error(error)
    finally:
        if connection:
            connection.close()


def get_new_model_version():
    try:
        connection = sqlite3.connect(get_model_registry_location() + '/models.db')
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


def persist_model(model):
    try:
        connection = sqlite3.connect(get_model_registry_location() + '/models.db')
        cursor = connection.cursor()

        query = '''INSERT INTO models
                            (name, version, created_at) VALUES (?, ?, ?)'''

        version = get_new_model_version()
        name = 'model-v{}'.format(version)
        created_at = str(time.time())

        cursor.execute(query, (name, version, created_at))

        content = model.read()

        with open(get_model_registry_location() + '/{}.joblib'.format(name), 'wb') as file:
            file.write(content)

        connection.commit()
        cursor.close()
    except sqlite3.Error as error:
        logger.get_logger().error('Error occured while inserting model')
        logger.get_logger().error(error)
    finally:
        if connection:
            connection.close()


def get_model_registry_location():
    if 'FLIXPREDIX_MREG' not in os.environ:
        logger.get_logger().error("Environment variable 'FLIXPREDIX_MREG' not set")
        return None

    return os.environ['FLIXPREDIX_MREG']


def load_active_model():
    model = get_active_model()

    return joblib.load(get_model_registry_location() + '/{}.joblib'.format(model.name))