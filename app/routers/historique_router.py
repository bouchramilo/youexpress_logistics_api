from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.historique_schema import Historique, HistoriqueCreate, HistoriqueUpdate
from app.services import historique_service, colis_service, livreur_service

router = APIRouter(prefix="/colis", tags=["historiques"])

# add historique status d'un colis
@router.post("/{colis_id}/historiques", response_model=Historique, status_code=status.HTTP_201_CREATED)
def create_historiques(colis_id: int, historique: HistoriqueCreate, db: Session = Depends(get_db)):
    db_colis = colis_service.show_colis(db, colis_id)
    if db_colis is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="colis non trouvé")
    if historique.livreur_id is not None:
        db_livreur = livreur_service.show_livreur(db, historique.livreur_id)
        if db_livreur is None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="livreur non trouvé")
    return historique_service.create_historique(db=db, historique=historique)

# get all historiques status d'un colis
@router.get("/{colis_id}/historiques", response_model=List[Historique])
def read_historique(colis_id: int, db: Session = Depends(get_db)):
    db_historiques = historique_service.index_historiques(db, colis_id)
    if db_historiques is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="historiques non trouvé")
    return db_historiques
