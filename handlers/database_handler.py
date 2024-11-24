import json
import os
import time
from uuid import uuid4

from global_variables import DEFAULT_PATH, DATABASES
from utilities.file_utilities import update_data


def create_database(database_name):
    """
    Create a database configuration and update the data file.
    """

    try:
        database_uid = create_database_folder()

        DEFAULT_DATA = {
            "name": database_name,
            "uid": database_uid,
            "created_at": int(time.time()),
            "indexes": []
        }

        update_data(database_uid, DEFAULT_DATA)

        return {
            "code": 200,
            "message": f"Your database {database_name} has been successfully created!"
        }
    except Exception as e:
        print(f"Exception on creating database: {e}")
        return {
            "code": 500,
            "message": f"NGDB has failed to create database {database_name}."
        }

def delete_database(database_name):
    # TODO: really delete database and indexes.

    try:
        del DATABASES[database_name]

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
    database_uid = str(uuid4())
    database_path = os.path.join(DEFAULT_PATH, database_uid)
    os.makedirs(database_path, exist_ok=True)
    return database_uid
