import pytest
from httpx import ASGITransport, AsyncClient

from app.database import check_db_health
from app.main import app


@pytest.mark.asyncio
async def test_health_endpoint_schema():
    """Verify endpoint response structure."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/health")
        assert response.status_code == 200
        data = response.json()
        assert "status" in data
        assert "database" in data
        assert data["version"] == "0.1.0"


@pytest.mark.asyncio
async def test_real_postgres_connectivity():
    """Execute real async SQL query against configured PostgreSQL instance."""
    is_connected = await check_db_health()
    assert is_connected is True, (
        "Failed to establish live connection to PostgreSQL database. "
        "Verify Docker container is up and healthy on the configured port."
    )

    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "ok"
        assert data["database"] == "connected"
