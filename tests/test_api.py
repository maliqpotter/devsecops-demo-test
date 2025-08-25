
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_crud_task():
    # Create
    payload = {"title": "Belajar FastAPI", "description": "Cek todo sederhana"}
    r = client.post("/tasks", json=payload)
    assert r.status_code == 201
    data = r.json()
    assert data["title"] == payload["title"]
    task_id = data["id"]

    # Get detail
    r = client.get(f"/tasks/{task_id}")
    assert r.status_code == 200
    assert r.json()["id"] == task_id

    # Update (partial)
    r = client.patch(f"/tasks/{task_id}", json={"completed": True})
    assert r.status_code == 200
    assert r.json()["completed"] is True

    # Toggle
    r = client.post(f"/tasks/{task_id}/toggle")
    assert r.status_code == 200
    assert r.json()["completed"] is False

    # Delete
    r = client.delete(f"/tasks/{task_id}")
    assert r.status_code == 204
