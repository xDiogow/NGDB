import json
import os
import time
from uuid import uuid4

from global_variables import DEFAULT_PATH, DATABASES
from utilities.file_utilities import update_data


def create_database(database_name: str) -> json:
    """
    Create a database configuration and update the data file.
    """

    try:
        # Creates the directory for the database and gets the UID of it.
        database_uid = create_database_folder()

        # Store data inside a variable
        DEFAULT_DATA = {
            "name": database_name,
            "uid": database_uid,
            "created_at": int(time.time()),
            "indexes": []
        }

        # Updates data in memory and physically
        update_data(database_uid, DEFAULT_DATA)

        # Returns a response to user
        return {
            "code": 200,
            "message": f"Your database {database_name} has been successfully created!"
        }
    except Exception as e:
        # Display error in logs
        print(f"Exception on creating database: {e}")

        # Returns a response to user
        return {
            "code": 500,
            "message": f"NGDB has failed to create database {database_name}."
        }

def delete_database(database_name: str) -> json:
    try:

        # Updates the memory
        del DATABASES[database_name]

        # Returns a response to user
        return {
            "code": 200,
            "message": f"Your database {database_name} has been successfully deleted!"
        }
    except KeyError:
        return {
            "code": 404,
            "message": f"Database {database_name} doesn't exist!"
        }

def create_database_folder() -> str:
    # Generates a Unique ID for the database
    database_uid = str(uuid4())

    # Stores the database path inside a variable
    database_path = os.path.join(DEFAULT_PATH, database_uid)

    # Creates the directory using the database path variable
    os.makedirs(database_path, exist_ok=True)

    # Returns the unique ID of the database
    return database_uid

def add_document(database_name: str) -> json:
    return {
        "code": 200,
        "message": f"Successfully added a new document in {database_name}!"
    }