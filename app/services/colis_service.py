from sqlalchemy.orm import Session
from app.models.colis import Colis
from app.models.historique import HistoriqueStatut
from app.schemas.colis_schema import ColisCreate
from app.schemas.colis_schema import ColisUpdate
from app.core.exceptions import BusinessException
from datetime import datetime
from typing import Optional, List

def create_colis(db: Session, colis: ColisCreate):
    if colis.poids <= 0:
        raise BusinessException("INVALID_WEIGHT", "Le poids du colis doit être supérieur à 0")
    
    if not colis.ville_destination:
        raise BusinessException("INVALID_DESTINATION", "La ville de destination est requise")
    
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
    
    # ###############################################""
    # cette partie pour l'ajout automatique de historique lors la crééation de colis
    # Créer automatiquement un historique avec le statut "CREE"
    historique = HistoriqueStatut(
        ancien_statut=None,
        nouveau_statut="CREE",
        colis_id=db_colis.id,
        livreur_id=None
    )
    db.add(historique)
    db.commit()
    # ###############################################""
    
    return db_colis


def update_colis(db : Session , colis_id : int ,  colis : ColisUpdate):
    db_colis = db.query(Colis).filter(Colis.id == colis_id).first()
    if not db_colis:
        raise BusinessException("COLIS_NOT_FOUND", f"Colis avec l'id {colis_id} n'existe pas")
    update_data = colis.model_dump(exclude_unset=True)
    for key , value in update_data:
        setattr(db_colis , key , value)
    
    db.commit()
    db.refresh(db_colis)
    return db_colis


def get_all_colis(db: Session, statut: Optional[str] = None, zone_id: Optional[int] = None) -> List[Colis]:
    query = db.query(Colis)
    
    if statut:
        query = query.filter(Colis.statut == statut)
    
    if zone_id:
        query = query.filter(Colis.zone_id == zone_id)
        
    return query.all()

def get_colis_by_id(db: Session, colis_id: int):
    db_colis = db.query(Colis).filter(Colis.id == colis_id).first()
    if not db_colis:
        raise BusinessException("COLIS_NOT_FOUND", f"Colis avec l'id {colis_id} n'existe pas")
    return db_colis

def update_colis(db: Session, colis_id: int, colis_update: ColisUpdate):
    db_colis = db.query(Colis).filter(Colis.id == colis_id).first()
    if not db_colis:
        raise BusinessException("COLIS_NOT_FOUND", f"Colis avec l'id {colis_id} n'existe pas")
    
    update_data = colis_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_colis, key, value)
    
    db.commit()
    db.refresh(db_colis)
    return db_colis

def assign_livreur_to_colis(db: Session, colis_id: int, livreur_id: int):
    db_colis = db.query(Colis).filter(Colis.id == colis_id).first()
    if not db_colis:
        raise BusinessException("COLIS_NOT_FOUND", f"Colis avec l'id {colis_id} n'existe pas")
    
    if db_colis.livreur_id is not None:
        raise BusinessException("COLIS_ALREADY_ASSIGNED", f"Colis {colis_id} est déjà assigné à un livreur")
    
    db_colis.livreur_id = livreur_id
    db_colis.statut = "EN_TRANSIT" 
    
    db.commit()
    db.refresh(db_colis)
    return db_colis