from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class Pothole(BaseModel):
    x: int
    y: int
    volume: float
    severity: str | None = None

@router.post("/")
def create_pothole(pothole: Pothole):
    return {"status": "success", "data": pothole}
