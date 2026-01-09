from sqlalchemy.orm import Session
from app.models.historique import HistoriqueStatut
from app.schemas.historique_schema import HistoriqueCreate, HistoriqueUpdate
from app.core.logging_config import get_logger
from app.core.exceptions import BusinessException

logger = get_logger("historique_service")


def create_historique(db: Session, colis_id: int, historique: HistoriqueCreate):
    logger.info(f"Création d'un nouvel historique pour le colis {colis_id} avec le statut '{historique.nouveau_statut}'")
    
    if not historique.nouveau_statut:
        raise BusinessException("INVALID_STATUS", "Le nouveau statut est requis")
    
    if colis_id <= 0:
        raise BusinessException("INVALID_COLIS_ID", "L'id du colis doit être supérieur à 0")
    
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
    
    if colis_id <= 0:
        raise BusinessException("INVALID_COLIS_ID", "L'id du colis doit être supérieur à 0")
    
    historiques = db.query(HistoriqueStatut).filter(HistoriqueStatut.colis_id == colis_id).all()
    logger.debug(f"Trouvé {len(historiques)} historiques pour le colis {colis_id}")
    return historiques

def get_all_historiques(db: Session, skip: int = 0, limit: int = 100):
    logger.debug(f"Récupération de tous les historiques (skip={skip}, limit={limit})")
    historiques = db.query(HistoriqueStatut).offset(skip).limit(limit).all()
    logger.debug(f"{len(historiques)} historiques récupérés")
    return historiques

def get_historique_by_id(db: Session, historique_id: int):
    logger.debug(f"Recherche de l'historique avec l'id {historique_id}")
    db_historique = db.query(HistoriqueStatut).filter(HistoriqueStatut.id == historique_id).first()
    if not db_historique:
        logger.warning(f"Historique avec l'id {historique_id} introuvable")
        raise BusinessException("HISTORIQUE_NOT_FOUND", f"Historique avec l'id {historique_id} n'existe pas")
    return db_historique


