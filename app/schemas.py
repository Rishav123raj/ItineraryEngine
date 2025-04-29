from pydantic import BaseModel
from typing import List, Optional

class HotelSchema(BaseModel):
    name: str
    location: str

class TransferSchema(BaseModel):
    from_location: str
    to_location: str
    mode: str

class ActivitySchema(BaseModel):
    name: str
    description: str

class DaySchema(BaseModel):
    day_number: int
    hotel: HotelSchema
    transfers: List[TransferSchema]
    activities: List[ActivitySchema]

class ItineraryCreate(BaseModel):
    name: str
    nights: int
    days: List[DaySchema]

class ItineraryOut(BaseModel):
    id: int
    name: str
    nights: int

    class Config:
        orm_mode = True
