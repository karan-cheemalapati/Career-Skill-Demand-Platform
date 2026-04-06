from fastapi.testclient import TestClient
from backend.app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()


def test_top_skills():
    response = client.get("/top-skills")
    assert response.status_code == 200
    data = response.json()
    assert "top_skills" in data
    assert isinstance(data["top_skills"], list)
    assert len(data["top_skills"]) > 0


def test_top_occupations():
    response = client.get("/top-occupations")
    assert response.status_code == 200
    data = response.json()
    assert "top_occupations" in data
    assert isinstance(data["top_occupations"], list)
    assert len(data["top_occupations"]) > 0


def test_valid_occupation():
    response = client.get("/occupation/11-1011")
    assert response.status_code == 200
    data = response.json()
    assert data["soc_code"] == "11-1011"
    assert "title" in data
    assert "top_skills" in data


def test_invalid_occupation():
    response = client.get("/occupation/invalid-code")
    assert response.status_code == 404
    assert response.json()["detail"] == "Occupation not found"