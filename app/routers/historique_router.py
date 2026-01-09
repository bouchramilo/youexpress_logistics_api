from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.historique_schema import Historique, HistoriqueCreate, HistoriqueUpdate
from app.services import historique_service, colis_service, livreur_service
from app.core.logging_config import get_logger

logger = get_logger("historique_router")

router = APIRouter(prefix="/colis", tags=["historiques"])

# add historique status d'un colis
@router.post("/{colis_id}/historiques", response_model=Historique, status_code=201)
def create_historiques(
    colis_id: int,
    historique: HistoriqueCreate,
    db: Session = Depends(get_db)
):
    logger.info(f"Demande de création d'historique pour le colis {colis_id}")
    
    db_colis = colis_service.get_colis_by_id(db, colis_id)
    if not db_colis:
        logger.warning(f"Tentative de création d'historique pour un colis inexistant (ID: {colis_id})")
        raise HTTPException(404, "colis non trouvé")

    if historique.livreur_id:
        db_livreur = livreur_service.show_livreur(db, historique.livreur_id)
        if not db_livreur:
            logger.warning(f"Tentative de création d'historique avec un livreur inexistant (ID: {historique.livreur_id})")
            raise HTTPException(404, "livreur non trouvé")

    logger.debug(f"Validation réussie pour le colis {colis_id} et livreur {historique.livreur_id}")
    return historique_service.create_historique(
        db=db,
        colis_id=colis_id,
        historique=historique
    )


# get all historiques status d'un colis
@router.get("/{colis_id}/historiques", response_model=List[Historique])
def read_historique(colis_id: int, db: Session = Depends(get_db)):
    logger.debug(f"Demande de récupération des historiques pour le colis {colis_id}")
    db_historiques = historique_service.index_historiques(db, colis_id)
    if db_historiques is None:
        logger.warning(f"Aucun historique trouvé pour le colis {colis_id}")
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="historiques non trouvé")
    logger.debug(f"{len(db_historiques)} historiques récupérés pour le colis {colis_id}")
    return db_historiques
