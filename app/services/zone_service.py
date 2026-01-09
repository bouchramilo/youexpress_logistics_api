from sqlalchemy.orm import Session
from app.models.zone import Zone
from app.schemas.zone_schema import ZoneCreate, ZoneUpdate
from app.core.logging_config import get_logger
from app.core.exceptions import BusinessException
from typing import List

logger = get_logger("zone_service")

def create_zone(db: Session, zone:ZoneCreate):
    logger.info(f"Création d'une nouvelle zone - Nom: {zone.nom}, Ville: {zone.ville}, Code postal: {zone.code_postal}")
    
    if not zone.nom:
        raise BusinessException("INVALID_NAME", "Le nom de la zone est requis")
    
    if not zone.ville:
        raise BusinessException("INVALID_CITY", "La ville de la zone est requise")
    
    existing_zone = db.query(Zone).filter(Zone.nom == zone.nom, Zone.ville == zone.ville).first()
    if existing_zone:
        raise BusinessException("ZONE_ALREADY_EXISTS", f"Une zone avec le nom '{zone.nom}' dans la ville '{zone.ville}' existe déjà")
    
    db_zone = Zone(**zone.model_dump())
    db.add(db_zone)
    db.commit()
    db.refresh(db_zone)
    
    logger.info(f"Zone créée avec succès (ID: {db_zone.id}) - Nom: {zone.nom}")
    return db_zone

def get_all_zones(db: Session, skip: int = 0, limit: int = 100) -> List[Zone]:
    logger.debug(f"Récupération de toutes les zones (skip={skip}, limit={limit})")
    zones = db.query(Zone).offset(skip).limit(limit).all()
    logger.debug(f"{len(zones)} zones récupérées")
    return zones

def get_zone_by_id(db: Session, zone_id: int) -> Zone:
    logger.debug(f"Recherche de la zone avec l'id {zone_id}")
    db_zone = db.query(Zone).filter(Zone.id == zone_id).first()
    if not db_zone:
        logger.warning(f"Zone avec l'id {zone_id} introuvable")
        raise BusinessException("ZONE_NOT_FOUND", f"Zone avec l'id {zone_id} n'existe pas")
    return db_zone