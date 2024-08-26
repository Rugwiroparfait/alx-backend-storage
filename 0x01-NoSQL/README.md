# README

## Project Overview

This project focuses on developing skills with NoSQL databases, particularly MongoDB. You will be required to perform various tasks to interact with MongoDB using both shell commands and Python scripts.

## Tasks

Below is a detailed list of tasks to be completed for this project, including the file names and expected outputs.

### Task 0: List All Databases

**Description:** Write a script that lists all databases in MongoDB.

- **File:** `0-list_databases`
- **Command Example:**
  ```sh
  cat 0-list_databases | mongo
  ```

### Task 1: Create a Database

**Description:** Write a script that creates or uses the database `my_db`.

- **File:** `1-use_or_create_database`
- **Command Example:**
  ```sh
  cat 1-use_or_create_database | mongo
  ```

### Task 2: Insert Document

**Description:** Write a script that inserts a document into the collection `school` with the attribute `name` set to "Holberton school".

- **File:** `2-insert`
- **Command Example:**
  ```sh
  cat 2-insert | mongo my_db
  ```

### Task 3: List All Documents

**Description:** Write a script that lists all documents in the collection `school`.

- **File:** `3-all`
- **Command Example:**
  ```sh
  cat 3-all | mongo my_db
  ```

### Task 4: List All Matches

**Description:** Write a script that lists all documents with `name="Holberton school"` in the collection `school`.

- **File:** `4-match`
- **Command Example:**
  ```sh
  cat 4-match | mongo my_db
  ```

### Task 5: Count Documents

**Description:** Write a script that displays the number of documents in the collection `school`.

- **File:** `5-count`
- **Command Example:**
  ```sh
  cat 5-count | mongo my_db
  ```

### Task 6: Update Document

**Description:** Write a script that adds a new attribute `address` with the value "972 Mission street" to documents in the collection `school` where `name="Holberton school"`.

- **File:** `6-update`
- **Command Example:**
  ```sh
  cat 6-update | mongo my_db
  ```

### Task 7: Delete by Match

**Description:** Write a script that deletes all documents with `name="Holberton school"` in the collection `school`.

- **File:** `7-delete`
- **Command Example:**
  ```sh
  cat 7-delete | mongo my_db
  ```

### Task 8: List All Documents in Python

**Description:** Write a Python function `list_all(mongo_collection)` that lists all documents in a collection. If no documents are present, return an empty list.

- **File:** `8-all.py`
- **Command Example:**
  ```sh
  python3 8-main.py
  ```

### Task 9: Insert Document in Python

**Description:** Write a Python function `insert_school(mongo_collection, **kwargs)` that inserts a new document in a collection and returns the new `_id`.

- **File:** `9-insert_school.py`
- **Command Example:**
  ```sh
  python3 9-main.py
  ```

### Task 10: Change School Topics

**Description:** Write a Python function `update_topics(mongo_collection, name, topics)` that changes all topics of a school document based on the `name`.

- **File:** `10-update_topics.py`
- **Command Example:**
  ```sh
  python3 10-main.py
  ```

### Task 11: Schools by Topic

**Description:** Write a Python function `schools_by_topic(mongo_collection, topic)` that returns a list of schools having a specific topic.

- **File:** `11-schools_by_topic.py`
- **Command Example:**
  ```sh
  python3 11-main.py
  ```

### Task 12: Log Stats

**Description:** Write a Python script `12-log_stats.py` that provides stats about Nginx logs stored in MongoDB. The script should display the number of logs, methods statistics, and count of `method=GET` with `path=/status`.

- **File:** `12-log_stats.py`
- **Command Example:**
  ```sh
  python3 12-log_stats.py
  ```

## Requirements

1. **MongoDB Command Files:**
   - Should be compatible with MongoDB 4.2.
   - Must end with a new line.
   - The first line should be a comment: `// my comment`.

2. **Python Scripts:**
   - Should be compatible with Python 3.7 and PyMongo 3.10.
   - Must start with `#!/usr/bin/env python3`.
   - Must end with a new line.
   - Follow `pycodestyle` style guidelines.
   - All modules and functions should be documented.
   - Scripts should not execute when imported.

## Installation

1. **Install MongoDB 4.2 on Ubuntu 18.04:**
   ```sh
   wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
   echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
   sudo apt-get update
   sudo apt-get install -y mongodb-org
   ```

2. **Install PyMongo:**
   ```sh
   pip3 install pymongo
   ```

3. **Create Data Directory (if necessary):**
   ```sh
   sudo mkdir -p /data/db
   ```

## License

Copyright © 2024 ALX. All rights reserved.
