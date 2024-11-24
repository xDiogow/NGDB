import json
import os
from utilities.file_utilities import get_default_path, update_data
from global_variables import DATABASES

def create_index(index_name, database_name):
    """
    Create an index for a specified database.
    """
    if database_name not in DATABASES:
        return {
            "code": 404,
            "message": f"Database {database_name} doesn't exist!"
        }

    database_uid = DATABASES[database_name]["uid"]
    database = DATABASES[database_name]
    database["name"] = database_name
    database["indexes"].append(index_name)
    update_data(database_uid, database)

    # Create an empty index file
    index_path = os.path.join(get_default_path(database_uid), f"{index_name}.json")
    with open(index_path, "w") as json_file:
        json.dump({}, json_file)

    return {
        "code": 200,
        "message": f"Your index {index_name} has been successfully created!"
    }