import pytest
from fastapi.testclient import TestClient
from main import app, store

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_store():
    store.reset()
    yield


def test_list_notes_empty():
    response = client.get("/notes")
    assert response.status_code == 200
    assert response.json() == []


def test_create_note():
    response = client.post("/notes", json={"title": "buy milk"})
    assert response.status_code == 201
    body = response.json()
    assert body["title"] == "buy milk"
    assert body["id"] == 1


def test_get_note():
    created = client.post("/notes", json={"title": "walk dog"}).json()
    response = client.get(f"/notes/{created['id']}")
    assert response.status_code == 200
    assert response.json()["title"] == "walk dog"


def test_get_note_not_found():
    response = client.get("/notes/999")
    assert response.status_code == 404


def test_update_note():
    created = client.post("/notes", json={"title": "old title"}).json()
    response = client.put(f"/notes/{created['id']}", json={"title": "new title"})
    assert response.status_code == 200
    assert response.json()["title"] == "new title"


def test_update_note_not_found():
    response = client.put("/notes/999", json={"title": "x"})
    assert response.status_code == 404


def test_delete_note():
    created = client.post("/notes", json={"title": "temp"}).json()
    response = client.delete(f"/notes/{created['id']}")
    assert response.status_code == 204
    assert client.get(f"/notes/{created['id']}").status_code == 404


def test_delete_note_not_found():
    response = client.delete("/notes/999")
    assert response.status_code == 404


def test_list_notes_pagination():
    for i in range(5):
        client.post("/notes", json={"title": f"note {i}"})
    response = client.get("/notes?limit=2&offset=1")
    assert response.status_code == 200
    titles = [n["title"] for n in response.json()]
    assert titles == ["note 1", "note 2"]
