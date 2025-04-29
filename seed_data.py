from app.models import Base, Itinerary, Day, Hotel, Transfer, Activity
from app.database import engine, SessionLocal

Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

db = SessionLocal()

itin = Itinerary(name="Phuket Escape", nights=3)
day1 = Day(day_number=1)
day1.hotel = Hotel(name="Andaman Resort", location="Phuket")
day1.activities = [Activity(name="Beach Time", description="Relax at Patong Beach")]
itin.days.append(day1)

db.add(itin)
db.commit()
db.close()
