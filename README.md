# open postgres db container in the terminal:
docker exec -it beneficiary_postgres psql -U postgres -d beneficiary_db

api logs: 
docker logs -f beneficiary_fastapi 

db logs:
docker logs -f beneficiary_postgres


# FastAPI + PostgreSQL Docker Project

## Project Overview

This project demonstrates how to containerize a FastAPI backend application with a PostgreSQL database using Docker and Docker Compose.

The application provides REST APIs to:

* Insert form data into PostgreSQL.
* Retrieve all submitted records.
* Automatically create the required database table during application startup.

---

# Tech Stack

* Python 3.11
* FastAPI
* PostgreSQL 16
* Docker
* Docker Compose
* Psycopg2
* Pydantic

---

# Project Structure

```
docker/
│
├── app/
│   ├── main.py
│   ├── db.py
│   ├── requirements.txt
│   └── .env
│
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# API Endpoints

## 1. Submit Form Data

**POST**

```
/submit-datadb
```

Stores form details in the PostgreSQL database.

---

## 2. Get All Form Data

**GET**

```
/get-form-data
```

Returns all records from the database.

---

# Docker Architecture

```
                    Docker Engine
                          │
        ┌─────────────────┴──────────────────┐
        │                                    │
        ▼                                    ▼
 FastAPI Container                 PostgreSQL Container
        │                                    │
        └──────────── Docker Network ────────┘
```

The FastAPI container communicates with the PostgreSQL container using the service name defined in `docker-compose.yml`.

```
DB_HOST=postgres
```

---

# Required Files

## 1. Dockerfile

Builds the FastAPI Docker image.

Responsibilities:

* Uses Python base image.
* Installs project dependencies.
* Copies application source code.
* Exposes port 8000.
* Starts the FastAPI application using Uvicorn.

---

## 2. docker-compose.yml

Creates and manages multiple containers.

Services:

* FastAPI
* PostgreSQL

Responsibilities:

* Builds FastAPI image.
* Pulls PostgreSQL image.
* Creates Docker network.
* Creates Docker volume.
* Starts both containers.

---

## 3. requirements.txt

Contains all Python dependencies.

Example:

```
fastapi
uvicorn
psycopg2-binary
python-dotenv
pydantic
email-validator
```

---

## 4. .env

Stores database configuration.

Example:

```
DB_HOST=postgres
DB_PORT=5432
DB_USER=postgres
DB_PASSWORD=edcsdatabase
DB_NAME=beneficiary_db
```

---

# Running the Project

## Step 1

Navigate to the project directory.

```
cd docker
```

---

## Step 2

Build the Docker image.

```
docker compose build
```

---

## Step 3

Start all containers.

```
docker compose up
```

or

```
docker compose up --build
```

---

## Step 4

Verify running containers.

```
docker ps
```

Expected containers:

```
beneficiary_fastapi
beneficiary_postgres
```

---

## Step 5

Open Swagger UI.

```
http://localhost:8000/docs
```

---

# Stopping Containers

```
docker compose down
```

---

# Viewing Logs

```
docker compose logs
```

Follow logs continuously:

```
docker compose logs -f
```

---

# Rebuilding the Application

If application code changes:

```
docker compose down
docker compose up --build
```

---

# Entering the PostgreSQL Container

```
docker exec -it beneficiary_postgres psql -U postgres -d beneficiary_db
```

---

# Useful PostgreSQL Commands

List databases:

```
\l
```

Connect to database:

```
\c beneficiary_db
```

List tables:

```
\dt
```

Describe table:

```
\d form_submission
```

View all records:

```sql
SELECT * FROM form_submission;
```

Count records:

```sql
SELECT COUNT(*) FROM form_submission;
```

Exit PostgreSQL:

```
\q
```

---

# Docker Commands

Build image:

```
docker compose build
```

Start containers:

```
docker compose up
```

Build and start:

```
docker compose up --build
```

Stop containers:

```
docker compose down
```

List running containers:

```
docker ps
```

List all containers:

```
docker ps -a
```

View container logs:

```
docker logs beneficiary_fastapi
```

View PostgreSQL logs:

```
docker logs beneficiary_postgres
```

Enter FastAPI container:

```
docker exec -it beneficiary_fastapi bash
```

Enter PostgreSQL container:

```
docker exec -it beneficiary_postgres bash
```

---

# Startup Flow

```
Developer
      │
      ▼
docker compose up --build
      │
      ▼
Docker Compose
      │
      ├──────────────┐
      ▼              ▼
FastAPI         PostgreSQL
Container       Container
      │              │
      │              ▼
      │      beneficiary_db
      │
      ▼
Application Startup
      │
      ▼
create_table()
      │
      ▼
Creates table if it does not exist
      │
      ▼
FastAPI starts listening on port 8000
```

---

# Database Connection

The FastAPI container connects to PostgreSQL using:

```
Host     : postgres
Port     : 5432
Database : beneficiary_db
Username : postgres
Password : edcsdatabase
```

---

# Features

* Dockerized FastAPI application
* Dockerized PostgreSQL database
* Environment variable configuration
* Automatic table creation on startup
* REST APIs for inserting and retrieving data
* Docker Compose orchestration
* Persistent PostgreSQL storage using Docker volumes

---

# Future Improvements

* SQLAlchemy ORM
* Alembic database migrations
* Nginx reverse proxy
* JWT authentication
* Health check endpoint
* Multi-stage Docker build
* CI/CD pipeline
* Production deployment on Ubuntu Server
* HTTPS with Nginx and SSL certificates
