from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional

from .. import schemas, models
from ..database import get_db
from ..services import recommendation_service

router = APIRouter()

@router.get("/", response_model=List[schemas.RecommendationResponse])
def get_recommendations(
    nights: int, 
    destination_id: Optional[int] = None, 
    db: Session = Depends(get_db)
):
    return recommendation_service.get_recommendations(db, nights, destination_id)
raise HTTPException(status_code=404, detail="No recommendations found")

# from fastapi import APIRouter, Depends, HTTPException
# from sqlalchemy.orm import Session
# from typing import List, Optional

# from .. import schemas, models
# from ..database import get_db
# from ..services import recommendation_service

# router = APIRouter()

# @router.get("/", response_model=List[schemas.RecommendationResponse])
# def get_recommendations(
#     nights: int, 
#     destination_id: Optional[int] = None, 
#     db: Session = Depends(get_db)
# ):
#     return recommendation_service.get_recommendations(db, nights, destination_id)