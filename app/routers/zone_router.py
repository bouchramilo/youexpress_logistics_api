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

@router.get("/", response_model=List[Zone])
def get_zones(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    logger.debug("Demande de récupération de toutes les zones")
    return zone_service.get_all_zones(db=db, skip=skip, limit=limit)

@router.get("/{zone_id}", response_model=Zone)
def get_zone(zone_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Demande de récupération de la zone {zone_id}")
    return zone_service.get_zone_by_id(db=db, zone_id=zone_id)
