from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app import models, schemas
from typing import List

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=schemas.ItineraryOut)
def create_itinerary(itinerary: schemas.ItineraryCreate, db: Session = Depends(get_db)):
    db_itinerary = models.Itinerary(name=itinerary.name, nights=itinerary.nights)
    db.add(db_itinerary)
    db.commit()
    db.refresh(db_itinerary)
    return db_itinerary

@router.get("/", response_model=List[schemas.ItineraryOut])
def get_itineraries(db: Session = Depends(get_db)):
    return db.query(models.Itinerary).all()
