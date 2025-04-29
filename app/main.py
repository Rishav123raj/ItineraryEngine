from fastapi import FastAPI
from app.routers import itinerary
from app.models import Base
from app.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Travel Itinerary API",
    description="Manages travel itineraries",
)

app.include_router(itinerary.router, prefix="/api/itineraries")
