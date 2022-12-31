import os
import json
import joblib
import numpy as np
import pandas as pd
import sklearn
import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData


def createModelTable():
    try:

        # Connect to DB and create a cursor
        connection = sqlite3.connect('example.db')
        cursor = connection.cursor()

        # Drop the hotel table if already exists.
        cursor.execute("DROP TABLE IF EXISTS hotel")

        print("DROPPING hotel TABLE")

        create_table = """CREATE TABLE hotel
            (ID INT PRIMARY KEY     NOT NULL,
            Active BOOLEAN NOT NULL CHECK (Active IN (0, 1)),
            Model BLOB,
            CreatedAt DATETIME DEFAULT CURRENT_TIMESTAMP); """

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

def insertModel(ID, Active, ModelFile):
    try:

            # Connect to DB and create a cursor
            connection = sqlite3.connect('example.db')
            cursor = connection.cursor()

            blob_query = """ INSERT INTO hotel
                                  (ID, Active, Model) VALUES (?, ?, ?)"""

            model = convertToBinaryData(ModelFile)

            data_tuple = (ID, Active, model) # will replace ? ? ?
            cursor.execute(blob_query, data_tuple)
            connection.commit()

            print("INSERTION SUCCESSFUL")

            print("All data in table\n")

            # create a cousor object for select query
            cursor.execute("SELECT * from hotel ")

            # display all data from hotel table
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


# When a new table is created, it is also reset
# createModelTable()

# Insert Models (ID, Active, ModelFile)
insertModel(3, False, "server/testBlob.txt")
