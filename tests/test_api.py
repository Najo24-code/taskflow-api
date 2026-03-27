"""API Tests"""
import pytest
from fastapi.testclient import TestClient
from main import app
from database import init_db

# Inicializar DB
init_db()

client = TestClient(app)

def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_health():
    """Test health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_docs():
    """Test OpenAPI docs"""
    response = client.get("/docs")
    assert response.status_code == 200

def test_auth_endpoints_exist():
    """Test auth endpoints respond"""
    response = client.post("/auth/login", data={"username": "x", "password": "x"})
    assert response.status_code in [401, 422]
    
    response = client.get("/auth/me")
    assert response.status_code == 401



def test_root():
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_health():
    """Test health endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_docs():
    """Test OpenAPI docs"""
    response = client.get("/docs")
    assert response.status_code == 200

def test_register_and_login():
    """Test user registration and login flow"""
    import random
    email = f"test{random.randint(1000,9999)}@test.com"
    
    # Register
    response = client.post("/auth/register", json={
        "email": email,
        "username": f"user{random.randint(1000,9999)}",
        "password": "testpass123"
    })
    assert response.status_code == 200
    
    # Login
    response = client.post("/auth/login", data={
        "username": email,
        "password": "testpass123"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()
