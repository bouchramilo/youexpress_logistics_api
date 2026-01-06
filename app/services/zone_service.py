from sqlalchemy.orm import Session
from app.models.zone import Zone
from app.schemas.zone_schema import ZoneCreate, ZoneUpdate

def create_zone(db: Session, zone:ZoneCreate):
    db_zone = Zone(**zone.model_dump())
    db.add(db_zone)
    db.commit()
    db.refresh(db_zone)
    return db_zone

def get_all_zones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Zone).offset(skip).limit(limit).all()