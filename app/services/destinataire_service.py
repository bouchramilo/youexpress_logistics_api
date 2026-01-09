from sqlalchemy.orm import Session
from app.models.destinataire import Destinataire
from app.schemas.destinataire import DestinataireCreate
from app.core.exceptions import BusinessException

def create_destinataire(db: Session, destinataire: DestinataireCreate) -> Destinataire:
    if not destinataire.nom:
        raise BusinessException("INVALID_NAME", "Le nom du destinataire est requis")
    
    if not destinataire.telephone:
        raise BusinessException("INVALID_PHONE", "Le téléphone du destinataire est requis")
    
    if not destinataire.adresse:
        raise BusinessException("INVALID_ADDRESS", "L'adresse du destinataire est requise")
    
    db_destinataire = Destinataire(
        nom=destinataire.nom,
        prenom=destinataire.prenom,
        email=destinataire.email,
        telephone=destinataire.telephone,
        adresse=destinataire.adresse
    )
    db.add(db_destinataire)
    db.commit()
    db.refresh(db_destinataire)
    return db_destinataire