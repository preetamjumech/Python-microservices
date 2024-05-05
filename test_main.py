from fastapi import FastAPI
from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Wikipdedia API. Call /search or /wiki"}


def test_read_phrase():
    response = client.get("/phrase/Jadavpur University (abbr.")
    assert response.status_code == 200
    assert response.json() == {"result": ["jadavpur"]}
