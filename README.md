<code>taskflow-api</code>

# TaskFlow — Project & Task Management System

[![Python 3.11+](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white&style=flat-square&labelColor=0d1117)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?logo=fastapi&logoColor=white&style=flat-square&labelColor=0d1117)](https://fastapi.tiangolo.com/)
[![JWT Auth](https://img.shields.io/badge/JWT-Auth-orange?style=flat-square&labelColor=0d1117)](https://jwt.io/)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?logo=docker&logoColor=white&style=flat-square&labelColor=0d1117)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=flat-square&labelColor=0d1117)](LICENSE)

A RESTful API for managing projects and tasks with user authentication, CRUD operations, and a responsive SPA frontend. Built with FastAPI, SQLAlchemy, and JWT authentication.

---

## $ quickstart

### Docker (recommended)

```bash
git clone https://github.com/Najo24-code/taskflow-api.git
cd taskflow-api
docker-compose up -d
```

Open http://localhost:8000

### Manual

```bash
git clone https://github.com/Najo24-code/taskflow-api.git
cd taskflow-api

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

uvicorn main:app --reload
```

---

## $ tree

```
taskflow-api/
├── main.py              # FastAPI entry point
├── auth.py              # JWT authentication
├── models.py            # SQLAlchemy models
├── schemas.py           # Pydantic schemas
├── database.py          # Database configuration
├── routes/
│   ├── __init__.py
│   └── items.py         # Items CRUD endpoints
├── frontend/
│   └── index.html       # SPA frontend
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_api.py
├── docs/                # Screenshots
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

---

## $ endpoints

### Authentication

| Method | Endpoint        | Description         |
|--------|-----------------|---------------------|
| POST   | `/auth/register`| Create a new account|
| POST   | `/auth/login`   | Log in and get JWT  |
| GET    | `/auth/me`      | Get current user    |

### Items

| Method | Endpoint        | Description         |
|--------|-----------------|---------------------|
| GET    | `/items/`       | List all items      |
| POST   | `/items/`       | Create a new item   |
| GET    | `/items/{id}`   | Get item by ID      |
| PUT    | `/items/{id}`   | Update an item      |
| DELETE | `/items/{id}`   | Delete an item      |

---

## $ env

| Variable          | Description            | Default                   |
|-------------------|------------------------|---------------------------|
| `DATABASE_URL`    | Database connection URL| `sqlite:///./data/app.db` |
| `JWT_SECRET`      | Secret key for JWT     | *(required)*              |
| `JWT_ALGORITHM`   | JWT signing algorithm  | `HS256`                   |

---

## $ test

```bash
pytest tests/ -v
```

---

## $ docker

```bash
# Build
docker build -t taskflow-api .

# Run
docker run -p 8000:8000 taskflow-api
```

---

## $ license

MIT © 2026 [Najo24-code](https://github.com/Najo24-code)
