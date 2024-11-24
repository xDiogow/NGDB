import json

from global_variables import DATABASES


def get_database_by_uid(database_uid) -> json:
    for db_name, db_data in DATABASES.items():
        if db_data["uid"] == database_uid:
            return {
                "code": 200,
                "data": {
                    "name": db_name,
                    **db_data
                }
            }

    return {
        "code": 404,
        "message": f"No database found with UID: {database_uid}"
    }

def get_database_uid_by_name(database_name) -> json:
    return DATABASES[database_name]["uid"]

def database_exists(database_name) -> bool:
    return database_name in DATABASES