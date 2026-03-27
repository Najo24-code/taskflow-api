"""API Tests"""
import pytest
import random
from fastapi.testclient import TestClient
from main import app
from database import init_db

init_db()
client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_docs():
    response = client.get("/docs")
    assert response.status_code == 200

def test_auth_endpoints_exist():
    response = client.post("/auth/login", data={"username": "x", "password": "x"})
    assert response.status_code in [401, 422]
    response = client.get("/auth/me")
    assert response.status_code in [401, 403]

def test_register_and_login():
    email = f"test{random.randint(1000,9999)}@test.com"
    response = client.post("/auth/register", json={
        "email": email,
        "username": f"user{random.randint(1000,9999)}",
        "password": "testpass123"
    })
    assert response.status_code == 200
    response = client.post("/auth/login", data={
        "username": email,
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
