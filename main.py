"""
NGDB (Not Good Database)
"""
import logging
from flask import Flask, request
from global_variables import DATABASES
from handlers.database_handler import create_database, delete_database
from handlers.document_handler import add_document
from handlers.index_handler import create_index
from utilities.global_utilities import find_databases

app = Flask(__name__)
logger = logging.getLogger(__name__)

@app.route("/", methods=["GET"])
def ping():
    return {
        "code": 200,
        "message": "Your server NGDB is ready to use."
    }

@app.route("/create_database", methods=["POST"])
def create_database_route():
    content = request.json
    database_name = content["name"]

    if database_name in DATABASES:
        return {
            "code": 409,
            "message": f"Database {database_name} already exists!"
        }

    return create_database(database_name)

@app.route("/create_index", methods=["POST"])
def create_index_route():
    content = request.json
    index_name = content["name"]
    database_name = content["database"]

    return create_index(index_name, database_name)

@app.route("/delete_database", methods=["DELETE"])
def delete_database_route():
    content = request.json
    database_name = content["database"]

    return delete_database(database_name)

@app.route("/add_document", methods=["POST"])
def add_document_route():
    content = request.json
    index_name = content["name"]
    database_name = content["database"]

    return add_document(database_name, index_name)

@app.route("/get_databases", methods=["GET"])
def get_databases():
    if not DATABASES:
        return {
            "code": 404,
            "message": "No databases found."
        }

    return {
        "code": 200,
        "message": "Databases retrieved successfully.",
        "data": DATABASES
    }

if __name__ == "__main__":
    DATABASES.update(find_databases())
    app.run(debug=True)
