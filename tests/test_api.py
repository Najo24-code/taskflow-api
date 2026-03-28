"""API Tests"""
import pytest
import random
from database import Base, engine
import models
from main import app
from fastapi.testclient import TestClient

# Crear tablas frescas
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

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

def test_auth_login_rejects_bad_creds():
    response = client.post("/auth/login", json={"email": "x", "password": "x"})
    assert response.status_code in [401, 422]

def test_auth_me_requires_token():
    response = client.get("/auth/me")
    assert response.status_code in [401, 403]

def test_register_and_login():
    email = f"test{random.randint(10000,99999)}@test.com"
    response = client.post("/auth/register", json={
        "email": email,
        "username": f"user{random.randint(10000,99999)}",
        "password": "testpass123"
    })
    assert response.status_code == 200, f"Register failed: {response.json()}"
    response = client.post("/auth/login", json={
        "email": email,
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
