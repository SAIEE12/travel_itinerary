from sqlalchemy.orm import Session
from typing import List, Optional

from .. import schemas, models

def get_recommendations(db: Session, nights: int, destination_id: Optional[int] = None):
    query = db.query(models.Itinerary).filter(
        models.Itinerary.duration_nights == nights,
        models.Itinerary.is_recommended == True
    )
    
    if destination_id:
        query = query.filter(models.Itinerary.destination_id == destination_id)
    
    itineraries = query.all()
    
    recommendations = []
    for it in itineraries:
        highlights = []
        for day in it.days:
            for act in day.activities:
                highlights.append(act.activity.name)
                if len(highlights) >= 3:
                    break
            if len(highlights) >= 3:
                break
        
        recommendations.append({
            "id": it.id,
            "name": it.name,
            "duration_nights": it.duration_nights,
            "description": it.description,
            "highlights": highlights[:3]
        })
    
    return recommendations