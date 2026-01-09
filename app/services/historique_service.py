from sqlalchemy.orm import Session
from app.models.historique import HistoriqueStatut
from app.schemas.historique_schema import HistoriqueCreate, HistoriqueUpdate
from app.core.logging_config import get_logger

logger = get_logger("historique_service")


def create_historique(db: Session, colis_id: int, historique: HistoriqueCreate):
    logger.info(f"Création d'un nouvel historique pour le colis {colis_id} avec le statut '{historique.nouveau_statut}'")
    
    # Récupérer le dernier historique du colis pour mettre à jour l'ancien_statut
    dernier_historique = db.query(HistoriqueStatut).filter(
        HistoriqueStatut.colis_id == colis_id
    ).order_by(HistoriqueStatut.id.desc()).first()
    
    # Si un historique existe, utiliser son nouveau_statut comme ancien_statut
    ancien_statut = None
    if dernier_historique:
        ancien_statut = dernier_historique.nouveau_statut
        logger.debug(f"Dernier statut trouvé: '{ancien_statut}' - Transition vers '{historique.nouveau_statut}'")
    else:
        logger.debug(f"Aucun historique précédent trouvé - Premier statut du colis")
    
    db_historique = HistoriqueStatut(
        ancien_statut=ancien_statut,
        nouveau_statut=historique.nouveau_statut,
        colis_id=colis_id,
        livreur_id=historique.livreur_id
    )
    db.add(db_historique)
    db.commit()
    db.refresh(db_historique)
    
    logger.info(f"Historique créé avec succès (ID: {db_historique.id}) - Colis: {colis_id}, Ancien: {ancien_statut}, Nouveau: {historique.nouveau_statut}")
    return db_historique


def index_historiques(db: Session, colis_id: int):
    logger.debug(f"Récupération de tous les historiques pour le colis {colis_id}")
    historiques = db.query(HistoriqueStatut).filter(HistoriqueStatut.colis_id == colis_id).all()
    logger.debug(f"Trouvé {len(historiques)} historiques pour le colis {colis_id}")
    return historiques


