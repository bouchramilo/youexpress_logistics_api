from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.zone_schema import Zone, ZoneCreate, ZoneUpdate
from app.services import zone_service
from app.core.logging_config import get_logger

logger = get_logger("zone_router")

router = APIRouter(prefix="/zones", tags=["zones"])

@router.post("/", response_model=Zone, status_code=status.HTTP_201_CREATED)
def create_zones(zone: ZoneCreate, db: Session = Depends(get_db)):
    logger.info(f"Demande de création d'une zone - Nom: {zone.nom}")
    return zone_service.create_zone(db=db, zone=zone)
