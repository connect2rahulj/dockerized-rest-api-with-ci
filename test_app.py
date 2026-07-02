import pytest
from app import app, tasks


@pytest.fixture(autouse=True)
def clear_tasks():
    """Reset task list and ID counter before each test."""
    import app as app_module
    app_module.tasks.clear()
    app_module.next_id = 1
    yield


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_tasks_empty(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []


def test_create_task(client):
    response = client.post(
        "/tasks",
        json={"title": "Test task"},
    )
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Test task"
    assert data["done"] is False
    assert data["id"] == 1


def test_create_task_missing_title(client):
    response = client.post("/tasks", json={})
    assert response.status_code == 400


def test_get_task_by_id(client):
    client.post("/tasks", json={"title": "Hello"})
    response = client.get("/tasks/1")
    assert response.status_code == 200
    assert response.get_json()["title"] == "Hello"


def test_get_task_not_found(client):
    response = client.get("/tasks/999")
    assert response.status_code == 404


def test_delete_task(client):
    client.post("/tasks", json={"title": "Delete me"})
    response = client.delete("/tasks/1")
    assert response.status_code == 200
    assert client.get("/tasks/1").status_code == 404


def test_get_all_tasks(client):
    client.post("/tasks", json={"title": "Task 1"})
    client.post("/tasks", json={"title": "Task 2"})
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.get_json()) == 2