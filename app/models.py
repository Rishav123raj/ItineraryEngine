from sqlalchemy import Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Itinerary(Base):
    __tablename__ = 'itineraries'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    nights = Column(Integer, nullable=False)
    days = relationship("Day", back_populates="itinerary")

class Day(Base):
    __tablename__ = 'days'
    id = Column(Integer, primary_key=True)
    day_number = Column(Integer, nullable=False)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    itinerary = relationship("Itinerary", back_populates="days")
    hotel = relationship("Hotel", back_populates="day", uselist=False)
    transfers = relationship("Transfer", back_populates="day")
    activities = relationship("Activity", back_populates="day")

class Hotel(Base):
    __tablename__ = 'hotels'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    location = Column(String)
    day_id = Column(Integer, ForeignKey("days.id"))
    day = relationship("Day", back_populates="hotel")

class Transfer(Base):
    __tablename__ = 'transfers'
    id = Column(Integer, primary_key=True)
    from_location = Column(String)
    to_location = Column(String)
    mode = Column(String)
    day_id = Column(Integer, ForeignKey("days.id"))
    day = relationship("Day", back_populates="transfers")

class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    day_id = Column(Integer, ForeignKey("days.id"))
    day = relationship("Day", back_populates="activities")
