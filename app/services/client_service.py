from sqlalchemy.orm import Session
from app.models.client import Client
from app.schemas.client import ClientCreate

def create_client(db: Session, client: ClientCreate) -> Client:
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
