from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.zone_schema import Zone, ZoneCreate, ZoneUpdate
from app.services import zone_service

router = APIRouter(prefix="/zones", tags=["zones"])

@router.post("/", response_model=Zone, status_code=status.HTTP_201_CREATED)
def create_zones(zone: ZoneCreate, db: Session = Depends(get_db)):
    return zone_service.create_zone(db=db, zone=zone)

@router.get("/", response_model=List[Zone])
def read_zones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return zone_service.get_all_zones(db, skip=skip, limit=limit)
