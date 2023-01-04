import os
import json
import joblib
import numpy as np
import pandas as pd
import sklearn
import sqlite3
import csv_to_sqlite 


def CSVtoSQL():
    options = csv_to_sqlite.CsvOptions(typing_style="full", encoding="windows-1250") 
    input_files = ["data/normalized.csv"] # pass in a list of CSV files
    csv_to_sqlite.write_csv(input_files, "data/normalized.db", options)

def createModelTable():
    try:

        # Connect to DB and create a cursor
        connection = sqlite3.connect('models.db')
        cursor = connection.cursor()

        # Drop the available table if already exists.
        cursor.execute("DROP TABLE IF EXISTS available")

        print("DROPPING available TABLE")

        create_table = """CREATE TABLE available
            (Name TEXT NOT NULL,
            Version INTEGER PRIMARY KEY NOT NULL,
            CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP,
            Active BOOLEAN NOT NULL CHECK (Active IN (0, 1)));"""

        connection.execute(create_table)

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

def insertModel(Name, Version, CreatedAt, Active):
    try:

            # Connect to DB and create a cursor
            connection = sqlite3.connect('models.db')
            cursor = connection.cursor()

            blob_query = """INSERT INTO available
                                  (Name, Version, CreatedAt, Active) VALUES (?, ?, ?, ?)"""

            data_tuple = (Name, Version, CreatedAt, Active) # will replace ? ?
            cursor.execute(blob_query, data_tuple)
            connection.commit()

            print("INSERTION SUCCESSFUL")

            print("All data in table\n")

            # create a cousor object for select query
            cursor.execute("SELECT * from available ")

            # display all data from available table
            for row in cursor:
                print(row)

            # Close the cursor
            cursor.close()

    # Handle errors
    except sqlite3.Error as error:
        print('Error occured at inserting - ', error)

    # Close DB Connection irrespective of success
    # or failure
    finally:
        if connection:
            connection.close()
            print('SQLite Connection closed')

def getModels():
    # Gets as JSON
    try:

            # Connect to DB and create a cursor
            connection = sqlite3.connect('models.db')
            cursor = connection.cursor()
            
            print("All data in table\n")

            # create a cousor object for select query
            cursor.execute("SELECT * from available ")

            # display all data from available table
            
            json_data = json.dumps(cursor.fetchall())

            print(json_data)

            cursor.close()
            return json_data

    # Handle errors
    except sqlite3.Error as error:
        print('Error occured at getting models - ', error)

    # Close DB Connection irrespective of success
    # or failure
    finally:
        if connection:
            connection.close()
            print('SQLite Connection closed')


# When a new table is created, it is also reset
createModelTable()

# Insert Models (name, version, date, active)
insertModel("model-v1", 1, 1670680824, False)
insertModel("model-v2", 2, 1670769070, True)

CSVtoSQL()