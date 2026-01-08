from sqlalchemy.orm import Session
from app.models.colis import Colis
from app.schemas.colis_schema import ColisCreate
from app.schemas.colis_schema import ColisUpdate
from datetime import datetime

def create_colis(db: Session, colis: ColisCreate):
    db_colis = Colis(
        
        description=colis.description,
        poids=colis.poids,
        statut=colis.statut,
        ville_destination=colis.ville_destination,
        date_creation=datetime.now(),
        client_id=colis.client_id,
        destinataire_id=colis.destinataire_id  
    )
    db.add(db_colis)
    db.commit()
    db.refresh(db_colis)
    return db_colis


def update_colis(db : Session , colis_id : int ,  colis : ColisUpdate):
    db_colis = db.query(Colis).filter(Colis.id == colis_id).first()
    if not db_colis:
        return None
    update_data = colis.model_dump(exclude_unset=True)
    for key , value in update_data:
        setattr(db_colis , key , value)
    
    db.commit()
    db.refresh(db_colis)
    return db_colis