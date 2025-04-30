from sqlalchemy.orm import Session
from app.database import SessionLocal, engine
from app import models

models.Base.metadata.create_all(bind=engine)

def seed_database():
    db = SessionLocal()
    
    try:
        # Destinations
        phuket = models.Destination(
            name="Phuket",
            region="Thailand",
            description="Thailand's largest island with beautiful beaches"
        )
        krabi = models.Destination(
            name="Krabi",
            region="Thailand",
            description="Famous for stunning limestone cliffs"
        )
        db.add_all([phuket, krabi])
        db.commit()
        
        # Hotels
        phuket_hotels = [
            models.Hotel(name="Luxury Beach Resort", destination_id=phuket.id, rating=4.8, price_per_night=200),
            models.Hotel(name="Boutique Hotel", destination_id=phuket.id, rating=4.2, price_per_night=120),
        ]
        krabi_hotels = [
            models.Hotel(name="Cliffside Resort", destination_id=krabi.id, rating=4.7, price_per_night=180),
            models.Hotel(name="Eco Lodge", destination_id=krabi.id, rating=4.0, price_per_night=90),
        ]
        db.add_all(phuket_hotels + krabi_hotels)
        db.commit()
        
        # Activities
        phuket_activities = [
            models.Activity(name="Phi Phi Island Tour", destination_id=phuket.id, duration_hours=8, price=50),
            models.Activity(name="Old Town Walking Tour", destination_id=phuket.id, duration_hours=3, price=20),
        ]
        krabi_activities = [
            models.Activity(name="Railay Beach Visit", destination_id=krabi.id, duration_hours=6, price=40),
            models.Activity(name="Emerald Pool Tour", destination_id=krabi.id, duration_hours=4, price=30),
        ]
        db.add_all(phuket_activities + krabi_activities)
        db.commit()
        
        # Recommended itineraries (2-8 nights)
        for nights in range(2, 9):
            # Phuket itinerary
            phuket_it = models.Itinerary(
                name=f"Phuket {nights}-Day Adventure",
                destination_id=phuket.id,
                duration_nights=nights,
                description=f"Our recommended {nights}-day itinerary for Phuket",
                is_recommended=True
            )
            db.add(phuket_it)
            db.commit()
            
            # Add days and activities
            for day_num in range(1, nights+1):
                day = models.ItineraryDay(
                    itinerary_id=phuket_it.id,
                    day_number=day_num
                )
                db.add(day)
                db.commit()
                
                # Add accommodation
                acc = models.Accommodation(
                    day_id=day.id,
                    hotel_id=phuket_hotels[day_num % len(phuket_hotels)].id
                )
                db.add(acc)
                
                # Add activities
                for i in range(2):  # 2 activities per day
                    act = models.ItineraryActivity(
                        day_id=day.id,
                        activity_id=phuket_activities[(day_num+i) % len(phuket_activities)].id,
                        start_time=f"{9+i*3}:00"
                    )
                    db.add(act)
                
                db.commit()
    finally:
        db.close()

if __name__ == "__main__":
    seed_database()