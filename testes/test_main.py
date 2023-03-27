import httpx
import pytest
from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

@pytest.mark.asyncio
async def test_upload_cnab():
    async with httpx.AsyncClient(app=app, base_url="http://test") as ac:
        with open("tests/sample_cnab.txt", "rb") as f:
            response = await ac.post("/upload/", files={"file": ("sample_cnab.txt", f, "text/plain")})
    assert response.status_code == 200
    assert response.json() == {"message": "Arquivo CNAB processado com sucesso"}

def test_read_transactions():
    response = client.get("/transactions/")
    assert response.status_code == 200
    transactions = response.json()
    assert len(transactions) > 0