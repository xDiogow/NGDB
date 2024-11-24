# NGDB (Not Good Database) 📦

NGDB is a lightweight, simple-to-use NoSQL database system designed for minimal use cases where traditional databases might feel like overkill. It’s **not good**—but it gets the job done (eventually)! 🚀

---

## Features 🌟

- 📂 **Create and manage databases** dynamically through a simple API.
- 📊 **Add and manage indexes** within databases.
- ✅ **Minimal setup**: No configuration required.
- 💾 **JSON-based storage**: Simplicity over complexity.

---

## Installation 🛠️

### 1. Clone the repository
```bash
git clone https://github.com/xDiogow/NGDB.git
cd NGDB
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the server
```bash
python main.py
```

---

## Usage 📝

### 1. **Check if the server is running**
Send a `GET` request to the root endpoint:
```bash
curl -X GET http://127.0.0.1:5000/
```

**Response**:
```json
{
    "code": 200,
    "message": "Your server NGDB is ready to use."
}
```

---

### 2. **Create a Database**
Send a `POST` request to create a new database:
```bash
curl -X POST http://127.0.0.1:5000/create_database -H "Content-Type: application/json" -d '{"name": "test_db"}'
```

**Response**:
```json
{
    "code": 200,
    "message": "Your database test_db has been successfully created!"
}
```

---

### 3. **Delete a Database**
Send a `DELETE` request to remove a database:
```bash
curl -X DELETE http://127.0.0.1:5000/delete_database -H "Content-Type: application/json" -d '{"database": "test_db"}'
```

**Response**:
```json
{
    "code": 200,
    "message": "Your database test_db has been successfully deleted!"
}
```

---

### 4. **Create an Index**
Send a `POST` request to create an index in a specific database:
```bash
curl -X POST http://127.0.0.1:5000/create_index -H "Content-Type: application/json" -d '{"index_name": "test_index", "database": "test_db"}'
```

**Response**:
```json
{
    "code": 200,
    "message": "Your index test_index has been successfully created!"
}
```

---

### 5. **Add a Document**
Send a `POST` request to add a document to an index:
```bash
curl -X POST http://127.0.0.1:5000/add_document -H "Content-Type: application/json" -d '{"index_name": "test_index", "database": "test_db", "content": {"key": "value"}}'
```

**Response**:
```json
{
    "code": 200,
    "message": "Your document has been successfully added!"
}
```

---

### 6. **Get Databases**
Send a `GET` request to retrieve all databases:
```bash
curl -X GET http://127.0.0.1:5000/get_databases
```

**Response**:
```json
{
  "code": 200,
  "message": "Databases retrieved successfully.",
  "data": {
    "test_db": {
      "created_at": 1732477443,
      "indexes": ["test_index"],
      "uid": "46981b26-dbed-44d8-945d-50e2e105327e"
    }
  }
}
```

---

## Directory Structure 📂

```
NGDB/
├── handlers/               # Core logic for database and index operations
│   ├── database_handler.py
│   ├── index_handler.py
│   ├── document_handler.py
├── utilities/              # Utility functions for file handling
│   ├── global_utilities.py
├── global_variables.py     # Global variables (e.g., DATABASES)
├── main.py                 # Main Flask application entry point
├── requirements.txt        # Python dependencies
└── README.md               # This file!
```

---

## Current Limitations ⚠️

- **Scalability**: NGDB is not designed for high-performance or large-scale data operations.
- **No advanced features**: Limited to basic database and index creation for now.

---

## Contributing 🤝

We welcome contributions! If you’d like to help, feel free to:
- Fork the repository.
- Create a new branch for your feature or bug fix.
- Submit a pull request.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Remember**: It’s **Not Good**, but it’s NGDB. 😉
