import os
import json
from global_variables import DEFAULT_PATH, DATABASES
from utilities.database_utilities import get_database_by_uid


def get_data_path(database_uid):
    return os.path.join(DEFAULT_PATH, database_uid, "data.json")

def get_default_path(database_uid):
    return os.path.join(DEFAULT_PATH, database_uid)

def get_folder_names(directory):
    """
    Get the names of all folders in the given directory.
    """
    return [
        item for item in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, item))
    ]

def update_data(database_uid, new_config):
    """
    Update the database configuration file and refresh the DATABASES dictionary.
    """

    # Gets the path to the data
    config_path = get_data_path(database_uid)

    try:
        # Updates the data physically
        with open(config_path, 'w') as file:
            json.dump(new_config, file)

        # Updates the data in memory
        update_local_data(database_uid, new_config)
        return True
    except IOError as e:
        # To change?
        raise IOError(f"Error writing to data.json: {e}")

def update_local_data(database_uid, data):
    global DATABASES

    if "name" not in data:
        raise KeyError("The 'name' field is required.")

    database_name = data["name"]
    DATABASES[database_name] = {"uid": database_uid}

    for key, value in data.items():
        if key != "name":
            DATABASES[database_name][key] = value

def load_data(database_uid):
    """
    Load the configuration for a database.
    """
    config_path = get_data_path(database_uid)
    try:
        with open(config_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        raise IOError(f"Error reading the file {config_path}: {e}")
