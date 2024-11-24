import os
import json
from global_variables import DEFAULT_PATH


def get_data_path(database_uid):
    return os.path.join(DEFAULT_PATH, database_uid, "data.json")

def get_index_data_path(database_uid, index_name):
    return os.path.join(DEFAULT_PATH, database_uid, index_name + ".json")


def get_default_path(database_uid):
    return os.path.join(DEFAULT_PATH, database_uid)

def get_folder_names(directory) -> list:
    """
    Get the names of all folders in the given directory.
    """
    return [
        item for item in os.listdir(directory)
        if os.path.isdir(os.path.join(directory, item))
    ]

def update_data(database_uid, new_data) -> bool:
    """
    Update the database configuration file and refresh the DATABASES dictionary.
    """

    # Gets the path to the data
    data_path = get_data_path(database_uid)

    try:
        # Updates the data physically
        with open(data_path, 'w') as file:
            json.dump(new_data, file)

        # Updates the data in memory
        update_local_data(database_uid, new_data)
        return True
    except IOError as e:
        # To change?
        raise IOError(f"Error writing to data.json: {e}")


# maybe make this return something?
def update_local_data(database_uid, data) -> None:
    global DATABASES

    if "name" not in data:
        raise KeyError("The 'name' field is required.")

    database_name = data["name"]
    DATABASES[database_name] = {"uid": database_uid}

    for key, value in data.items():
        if key != "name":
            DATABASES[database_name][key] = value

def load_data(database_uid) -> json:
    """
    Load the configuration for a database.
    """
    data_path = get_data_path(database_uid)
    try:
        with open(data_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        raise IOError(f"Error reading the file {data_path}: {e}")

def load_index_data(index_name, database_uid) -> json:
    """
    Load the configuration for a database.
    """
    data_path = get_index_data_path(database_uid, index_name)
    try:
        with open(data_path, 'r') as file:
            return json.load(file)
    except Exception as e:
        raise IOError(f"Error reading the file {data_path}: {e}")
