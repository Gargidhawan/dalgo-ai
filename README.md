# FastAPI Machine Learning API
## Overview
This service exposes an API for various machine-learning tasks, designed to be called by the Dalgo backend.
## Installation and Setup
### Prerequisites
• Python 3.6 or higher
• Pip (Python package installer)
## Setting up the project
### Clone the Repository
```bash
git clone <repository_url>
cd <repository_name>
```
Create and Activate Virtual Environment.
```bash
python -m venv venv
```
Activate your Virtual Environment using command depending on the system.\
On Windows:
```bash
.\venv\Scripts\activate
```
On Linux/Mac:
```bash
source venv/bin/activate
```
Install Dependencies
```bash
pip install -r requirements.txt
```
Run the Application
```bash
python main.py --port 8080
```
Now you can view your project at http://localhost:8080/

## Configuring MindsDB
Troubleshooting MindsDB Installation
If you encounter the `no module named mindsdb` issue,\
follow these steps to install MindsDB:
Install MindsDB via pip:
bash
`pip install mindsdb`
or
Install MindsDB using Docker:\
Refer to the MindsDB Docker setup guide at https://github.com/mindsdb/mindsdb and https://docs.mindsdb.com/setup/self-hosted/docker.\
Run the following command to start the MindsDB container:
```bash
docker run --name mindsdb_container -p 47334:47334 -p 47335:47335 mindsdb/mindsdb
```
Verify the running container at: http://127.0.0.1:47334

## Setting up A database (Postgres)
Now only thing left is to connect mindsDB with postgres.

install postgres from https://www.postgresql.org/download/ \
NOTE:- remember your username and password.

after installing verify postgres using
```bash
psql -U postgres
```

### creating a Database from project.
head to http://localhost:8080/docs/ \
there are 2 routes. \
create database using route `create_db` and required parameters. \
This route will help to create a database directly.
Also, instead of using a route you can create a database using postgres cli.\
Using `CREATE DATABASE <database_name>`




