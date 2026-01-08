from sqlalchemy.orm import Session
from app.models.destinataire import Destinataire
from app.schemas.destinataire import DestinataireCreate

def create_destinataire(db: Session, destinataire: DestinataireCreate) -> Destinataire:
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