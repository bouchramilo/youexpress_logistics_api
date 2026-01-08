from sqlalchemy.orm import Session
from app.models.historique import HistoriqueStatut
from app.schemas.historique_schema import HistoriqueCreate, HistoriqueUpdate


def create_historique(db: Session, historique:HistoriqueCreate):
    db_historique = HistoriqueStatut(**historique.model_dump())
    db.add(db_historique)
    db.commit()
    db.refresh(db_historique)
    return db_historique


def index_historiques(db: Session, colis_id: int):
    return db.query(HistoriqueStatut).filter(HistoriqueStatut.colis_id == colis_id).all()


