from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

def test_create_and_read_item():
    # Testa a criação de um item no banco SQLite
    response = client.post("/api/items", json={"title": "Testar Pipeline CI"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Testar Pipeline CI"
    assert "id" in data

    # Testa a listagem
    response = client.get("/api/items")
    assert response.status_code == 200
    assert len(response.json()) > 0
