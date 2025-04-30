from fastapi import FastAPI
from app.database import engine
from app import models
from app.api import itineraries, recommendations

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(
    itineraries.router,
    prefix="/itineraries",
    tags=["itineraries"]
)
app.include_router(
    recommendations.router,
    prefix="/recommendations",
    tags=["recommendations"]
)

@app.get("/")
def read_root():
    return {"message": "Travel Itinerary Management System"}