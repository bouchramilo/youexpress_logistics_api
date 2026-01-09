from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client import ClientCreate
from app.core.exceptions import BusinessException
from typing import List

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

def get_all_clients(db: Session, skip: int = 0, limit: int = 100) -> List[Client]:
    return db.query(Client).offset(skip).limit(limit).all()

def get_client_by_id(db: Session, client_id: int) -> Client:
    db_client = db.query(Client).filter(Client.id == client_id).first()
    if not db_client:
        raise BusinessException("CLIENT_NOT_FOUND", f"Client avec l'id {client_id} n'existe pas")
    return db_client
