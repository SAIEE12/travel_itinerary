from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .. import schemas, models
from ..database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Itinerary)
def create_itinerary(itinerary: schemas.ItineraryCreate, db: Session = Depends(get_db)):
    db_itinerary = models.Itinerary(
        name=itinerary.name,
        destination_id=itinerary.destination_id,
        duration_nights=itinerary.duration_nights,
        description=itinerary.description
    )
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    
    for day_data in itinerary.days:
        db_day = models.ItineraryDay(
            itinerary_id=db_itinerary.id,
            day_number=day_data.day_number
        )
        db.add(db_day)
        db.commit()
        db.refresh(db_day)
        
        for hotel_id in day_data.accommodations:
            db_accommodation = models.Accommodation(
                day_id=db_day.id,
                hotel_id=hotel_id
            )
            db.add(db_accommodation)
        
        for activity_id in day_data.activities:
            db_activity = models.ItineraryActivity(
                day_id=db_day.id,
                activity_id=activity_id
            )
            db.add(db_activity)
        
    return db_itinerary

@router.get("/", response_model=List[schemas.Itinerary])
def read_itineraries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    itineraries = db.query(models.Itinerary).offset(skip).limit(limit).all()
    return itineraries

@router.get("/{itinerary_id}", response_model=schemas.ItineraryDetail)
def read_itinerary(itinerary_id: int, db: Session = Depends(get_db)):
    itinerary = db.query(models.Itinerary).filter(models.Itinerary.id == itinerary_id).first()
    if not itinerary:
        raise HTTPException(status_code=404, detail="Itinerary not found")
    return itinerary