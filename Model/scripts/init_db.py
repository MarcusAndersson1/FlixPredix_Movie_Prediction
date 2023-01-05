import sqlite3

CREATE_REGISTERED = """CREATE TABLE models 
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE,
    version INTEGER NOT NULL UNIQUE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP);"""

CREATE_ACTIVE = """CREATE TABLE active
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    active INTEGER NOT NULL,
    FOREIGN KEY(active) REFERENCES models(version));
"""

def init_db():
    try:

        connection = sqlite3.connect('models/models.db')
        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS models")
        cursor.execute("DROP TABLE IF EXISTS active")

        cursor.execute(CREATE_REGISTERED)
        cursor.execute(CREATE_ACTIVE)

        # Close the cursor
        cursor.close()

    # Handle errors
    except sqlite3.Error as error:
        print('Error occured at creating table - ', error)

    # Close DB Connection irrespective of success
    # or failure
    finally:
        if connection:
            connection.close()
            print('SQLite Connection closed')


def insert_model(name, version, created_at):
    try:
        connection = sqlite3.connect('models/models.db')
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


def set_active_model(version):
    try:
        connection = sqlite3.connect('models/models.db')
        cursor = connection.cursor()

        query = """INSERT INTO active (active) VALUES (?)"""

        cursor.execute(query, (version,))
        connection.commit()

        cursor.close()

    except sqlite3.Error as error:
        print('Error occured while setting active model', error)

    finally:
        if connection:
            connection.close()

init_db()
insert_model('model-v1', 1, 1670680824)
insert_model('model-v2', 2, 1670769070)
set_active_model(2)