from sqlalchemy.orm import Session
from app.models.zone import Zone
from app.schemas.zone_schema import ZoneCreate, ZoneUpdate
from app.core.logging_config import get_logger

logger = get_logger("zone_service")

def create_zone(db: Session, zone:ZoneCreate):
    logger.info(f"Création d'une nouvelle zone - Nom: {zone.nom}, Ville: {zone.ville}, Code postal: {zone.code_postal}")
    
    db_zone = Zone(**zone.model_dump())
    db.add(db_zone)
    db.commit()
    db.refresh(db_zone)
    
    logger.info(f"Zone créée avec succès (ID: {db_zone.id}) - Nom: {zone.nom}")
    return db_zone