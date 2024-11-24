import json
import os.path
from uuid import uuid4

from utilities.database_utilities import get_database_uid_by_name
from utilities.file_utilities import get_default_path, load_index_data


def add_document(database_name: str, index_name: str, content: str) -> json:
    database_uid = get_database_uid_by_name(database_name)
    path = os.path.join(get_default_path(database_uid), index_name + ".json")

    entries = load_index_data(index_name, database_uid)
    with open(path, mode='w', encoding='utf-8') as file:
        entries.append(content)
        json.dump(entries, file)

    return {
        "code": 200,
        "message": f"Successfully added a new document in {database_name}!"
    }