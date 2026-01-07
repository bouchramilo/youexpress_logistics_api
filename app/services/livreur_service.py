from sqlalchemy.orm import Session
from app.models.livreur import Livreur
from app.schemas.livreur_schema import LivreurCreate, LivreurUpdate


def create_livreur(db: Session, livreur:LivreurCreate):
    db_livreur = Livreur(**livreur.model_dump())
    db.add(db_livreur)
    db.commit()
    db.refresh(db_livreur)
    return db_livreur


def index_livreurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Livreur).offset(skip).limit(limit).all()


def show_livreur(db: Session, livreur_id: int):
    return db.query(Livreur).filter(Livreur.id == livreur_id).first()