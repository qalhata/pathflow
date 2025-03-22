from fastapi import FastAPI
from backend.api import pothole_routes, ugv_routes

app = FastAPI()

app.include_router(pothole_routes.router, prefix="/api/potholes")
app.include_router(ugv_routes.router, prefix="/api/ugvs")

@app.get("/")
def read_root():
    return {"message": "Welcome to PathFlow API"}
