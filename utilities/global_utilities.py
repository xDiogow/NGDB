from utilities.file_utilities import get_folder_names, load_data
from global_variables import DEFAULT_PATH

def find_databases():
    """
    Scan for databases and populate the global DATABASES dictionary.
    """
    folders = get_folder_names(DEFAULT_PATH)
    databases = {}

    for database_uid in folders:
        data = load_data(database_uid)

        database_name = data["name"]
        databases[database_name] = {
            "uid": data["uid"],
            "indexes": data["indexes"],
            "created_at": data["created_at"]
        }
    return databases
