import pytest
from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Student Task Manager" in response.data


def test_add_task(client):
    response = client.post(
        "/add",
        data={"title": "Test Task"},
        follow_redirects=True
    )

    assert response.status_code == 200
    assert b"Test Task" in response.data


def test_complete_task(client):
    response = client.get(
        "/complete/1",
        follow_redirects=True
    )

    assert response.status_code == 200


def test_delete_task(client):
    response = client.get(
        "/delete/1",
        follow_redirects=True
    )

    assert response.status_code == 200