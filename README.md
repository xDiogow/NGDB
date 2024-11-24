# NGDB (Not Good Database) 📦

NGDB is a lightweight, simple-to-use nosql database system designed for minimal use cases where traditional databases might feel like overkill. It’s **not good**—but it gets the job done!
Project is not done, I am still working on it.

---

## Features 🚀

- Create and manage databases dynamically.
- Add and manage indexes within databases.
- Minimal configuration required > No configuration
- Stores data in JSON files for simplicity -> Doesn't store yet

---

## Installation 🛠️

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/NGDB.git
   cd NGDB
   ```
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**:
   ```bash
   python main.py
   ```

---

## Usage 📝

### 1. Create a Database
Send a `POST` request to create a database:
```bash
curl -X POST http://127.0.0.1:5000/create_database -H "Content-Type: application/json" -d '{"database": "test_db"}'
```

**Response**:
```json
{
    "code": 200,
    "message": "Your database test_db has been successfully created!"
}
```

### 2. Delete a Database
Send a `DELETE` request to create a database:
```bash
curl -X POST http://127.0.0.1:5000/create_database -H "Content-Type: application/json" -d '{"database": "test_db"}'
```

**Response**:
```json
{
    "code": 200,
    "message": "Your database test_db has been successfully deleted!"
}
```

---

### 3. Create an Index
Send a `POST` request to create an index in a specific database:
```bash
curl -X POST http://127.0.0.1:5000/create_index -H "Content-Type: application/json" -d '{"name": "test_index", "database": "test_db"}'
```

**Response**:
```json
{
    "code": 200,
    "message": "Your index test_index has been successfully created!"
}
```

---

### 4. Get Databases
Send a `GET` request to list all databases:
```bash
curl -X GET http://127.0.0.1:5000/get_databases
```

**Response**:
```json
{
  "code": 200,
  "data": {
    "test_db": {
      "created_at": 1732477443,
      "indexes": [
        "test_index1"
      ],
      "uid": "46981b26-dbed-44d8-945d-50e2e105327e"
    }
  },
  "message": "Databases retrieved successfully."
}
```

---

## Directory Structure 📂

```
NGDB/
├── handlers/               # Core logic for database and index operations
│   ├── database_handler.py
│   ├── index_handler.py
├── utilities/              # Utility functions for file handling
│   ├── file_utilities.py
│   ├── database_utilities.py
├── global_variables.py     # Global variables (e.g., DEFAULT_PATH, DATABASES)
├── main.py                 # Main Flask application entry point
└── README.md               # This file!
```

---

## Limitations ⚠️

- Not designed for high-performance or large-scale data operations.
- Stores data in JSON files, which might become slow as data grows.
- Not a replacement for traditional databases like MySQL, PostgreSQL, or MongoDB.

---

## Contributing 🤝

We welcome contributions! Feel free to fork the repository, make changes, and submit a pull request.

---

## License 📜

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

**Remember**: It’s **Not Good**, but it’s NGDB. 😉
