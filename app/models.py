from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship
from .database import Base

class Destination(Base):
    __tablename__ = "destinations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    region = Column(String)
    description = Column(String)

    hotels = relationship("Hotel", back_populates="destination")
    activities = relationship("Activity", back_populates="destination")
    itineraries = relationship("Itinerary", back_populates="destination")

class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    destination_id = Column(Integer, ForeignKey("destinations.id"))
    rating = Column(Float)
    price_per_night = Column(Float)

    destination = relationship("Destination", back_populates="hotels")
    accommodations = relationship("Accommodation", back_populates="hotel")

class Activity(Base):
    __tablename__ = "activities"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    destination_id = Column(Integer, ForeignKey("destinations.id"))
    duration_hours = Column(Float)
    price = Column(Float)
    description = Column(String)

    destination = relationship("Destination", back_populates="activities")
    itinerary_activities = relationship("ItineraryActivity", back_populates="activity")

class Itinerary(Base):
    __tablename__ = "itineraries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    destination_id = Column(Integer, ForeignKey("destinations.id"))
    duration_nights = Column(Integer)
    description = Column(String)
    is_recommended = Column(Boolean, default=False)

    destination = relationship("Destination", back_populates="itineraries")
    days = relationship("ItineraryDay", back_populates="itinerary")

class ItineraryDay(Base):
    __tablename__ = "itinerary_days"

    id = Column(Integer, primary_key=True, index=True)
    itinerary_id = Column(Integer, ForeignKey("itineraries.id"))
    day_number = Column(Integer)

    itinerary = relationship("Itinerary", back_populates="days")
    accommodations = relationship("Accommodation", back_populates="day")
    activities = relationship("ItineraryActivity", back_populates="day")
    transfers = relationship("Transfer", back_populates="day")

class Accommodation(Base):
    __tablename__ = "accommodations"

    id = Column(Integer, primary_key=True, index=True)
    day_id = Column(Integer, ForeignKey("itinerary_days.id"))
    hotel_id = Column(Integer, ForeignKey("hotels.id"))

    day = relationship("ItineraryDay", back_populates="accommodations")
    hotel = relationship("Hotel", back_populates="accommodations")

class ItineraryActivity(Base):
    __tablename__ = "itinerary_activities"

    id = Column(Integer, primary_key=True, index=True)
    day_id = Column(Integer, ForeignKey("itinerary_days.id"))
    activity_id = Column(Integer, ForeignKey("activities.id"))
    start_time = Column(String)

    day = relationship("ItineraryDay", back_populates="activities")
    activity = relationship("Activity", back_populates="itinerary_activities")

class Transfer(Base):
    __tablename__ = "transfers"

    id = Column(Integer, primary_key=True, index=True)
    day_id = Column(Integer, ForeignKey("itinerary_days.id"))
    from_location = Column(String)
    to_location = Column(String)
    transport_type = Column(String)
    duration_minutes = Column(Integer)

    day = relationship("ItineraryDay", back_populates="transfers")