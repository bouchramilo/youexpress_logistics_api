from sqlalchemy.orm import Session
from app.models.zone import Zone
from app.schemas.zone_schema import ZoneCreate, ZoneUpdate

def create_zone(db: Session, zone:ZoneCreate):
    db_zone = Zone(**zone.model_dump())
    db.add(db_zone)
    db.commit()
    db.refresh(db_zone)
    return db_zone