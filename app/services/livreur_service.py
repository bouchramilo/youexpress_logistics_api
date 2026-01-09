from sqlalchemy.orm import Session
from app.models.livreur import Livreur
from app.schemas.livreur_schema import LivreurCreate, LivreurUpdate
from app.core.exceptions import BusinessException


def create_livreur(db: Session, livreur:LivreurCreate):
    if not livreur.nom:
        raise BusinessException("INVALID_NAME", "Le nom du livreur est requis")
    
    if not livreur.telephone:
        raise BusinessException("INVALID_PHONE", "Le téléphone du livreur est requis")
    
    db_livreur = Livreur(**livreur.model_dump())
    db.add(db_livreur)
    db.commit()
    db.refresh(db_livreur)
    return db_livreur


def index_livreurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Livreur).offset(skip).limit(limit).all()


def show_livreur(db: Session, livreur_id: int):
    db_livreur = db.query(Livreur).filter(Livreur.id == livreur_id).first()
    if not db_livreur:
        raise BusinessException("LIVREUR_NOT_FOUND", f"Livreur avec l'id {livreur_id} n'existe pas")
    return db_livreur