from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class UGV(BaseModel):
    x: int
    y: int
    status: str = "idle"

@router.post("/")
def register_ugv(ugv: UGV):
    return {"status": "UGV registered", "data": ugv}

@router.get("/")
def list_ugvs():
    # Placeholder response; you'll eventually fetch this from the database
    return {"ugvs": [{"id": 1, "x": 5, "y": 3, "status": "idle"}]}
