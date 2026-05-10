import pytest
from app import create_app
from app.tasks.routes import state

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


@pytest.fixture(autouse=True)
def reset_state():
    state["tasks"].clear()
    state["tasks"].update({
        1: {"id": 1, "title": "setup project", "completed": True},
        2: {"id": 2, "title": "add metrics", "completed": False},
        3: {"id": 3, "title": "configure logging", "completed": False}
    })
    state["next_id"] = 4

def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}


def test_create_task(client):
    response = client.post("/tasks", json={"title":"test task"})

    assert response.status_code == 201

    data = response.get_json()
    assert data["title"] == "test task"
    assert data["completed"] is False


def test_get_task(client):
    create_response = client.post("/tasks", json={"title": "test"})
    assert create_response.status_code == 201

    task_id = create_response.get_json()["id"]

    get_response = client.get(f"/tasks/{task_id}")
    assert get_response.status_code == 200

    data = get_response.get_json()
    assert data["id"] == task_id
    assert data["title"] == "test"

def test_not_found(client):
    response = client.get("/tasks/999")

    assert response.status_code == 404
    assert response.get_json()["error"] == "task not found"

def test_delete_task(client):
    response = client.post("/tasks", json={"title": "delete me"})
    task_id = response.get_json()["id"]

    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200

    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404
