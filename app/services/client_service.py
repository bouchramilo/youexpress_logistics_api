from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client import ClientCreate
from app.core.exceptions import BusinessException

def create_client(db: Session, client: ClientCreate) -> Client:
    if not client.nom:
        raise BusinessException("INVALID_NAME", "Le nom du client est requis")
    
    if not client.email:
        raise BusinessException("INVALID_EMAIL", "L'email du client est requis")
    
    existing_client = db.query(Client).filter(Client.email == client.email).first()
    if existing_client:
        raise BusinessException("EMAIL_ALREADY_EXISTS", f"Un client avec l'email {client.email} existe déjà")
    
    db_client = Client(
        nom=client.nom,
        prenom=client.prenom,
        email=client.email,
        adresse=client.adresse,
        telephone=client.telephone,
        ville=client.ville,
    )
    db.add(db_client)
    db.commit()
    db.refresh(db_client)
    return db_client
