from fastapi import APIRouter
from pydantic import BaseModel

from app.database import check_db_health

router = APIRouter(tags=["health"])


class HealthResponse(BaseModel):
    status: str
    database: str
    version: str = "0.1.0"


@router.get("/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    db_ok = await check_db_health()
    return HealthResponse(
        status="ok" if db_ok else "degraded",
        database="connected" if db_ok else "disconnected",
    )
