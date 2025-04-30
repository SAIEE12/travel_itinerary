from typing import List, Optional
from pydantic import BaseModel

class HotelBase(BaseModel):
    name: str
    rating: Optional[float] = None
    price_per_night: Optional[float] = None

class HotelCreate(HotelBase):
    destination_id: int

class Hotel(HotelBase):
    id: int
    destination_id: int

    class Config:
        orm_mode = True

class ActivityBase(BaseModel):
    name: str
    duration_hours: Optional[float] = None
    price: Optional[float] = None
    description: Optional[str] = None

class ActivityCreate(ActivityBase):
    destination_id: int

class Activity(ActivityBase):
    id: int
    destination_id: int

    class Config:
        orm_mode = True

class DestinationBase(BaseModel):
    name: str
    region: str
    description: Optional[str] = None

class DestinationCreate(DestinationBase):
    pass

class Destination(DestinationBase):
    id: int
    hotels: List[Hotel] = []
    activities: List[Activity] = []

    class Config:
        orm_mode = True

class ItineraryDayBase(BaseModel):
    day_number: int

class ItineraryDayCreate(ItineraryDayBase):
    accommodations: List[int] = []
    activities: List[int] = []

class ItineraryDay(ItineraryDayBase):
    id: int
    itinerary_id: int

    class Config:
        orm_mode = True

class ItineraryBase(BaseModel):
    name: str
    duration_nights: int
    description: Optional[str] = None

class ItineraryCreate(ItineraryBase):
    destination_id: int
    days: List[ItineraryDayCreate] = []

class Itinerary(ItineraryBase):
    id: int
    destination_id: int
    is_recommended: bool
    days: List[ItineraryDay] = []

    class Config:
        orm_mode = True

class ItineraryDetail(Itinerary):
    destination: Destination

class RecommendationResponse(BaseModel):
    id: int
    name: str
    duration_nights: int
    description: str
    highlights: List[str]