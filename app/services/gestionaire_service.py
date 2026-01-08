from sqlalchemy.orm import Session
from app.models.gestionaire import Gestionaire  # Make sure this matches your model filename
from app.schemas.gestionaire_schema import GestionaireCreate

def create_gestionaire(db: Session, gestionaire_data: GestionaireCreate):
    db_gestionaire = Gestionaire(
        nom=gestionaire_data.nom,
        email=gestionaire_data.email,
        mot_de_passe=gestionaire_data.mot_de_passe
    )
    db.add(db_gestionaire)
    db.commit()
    db.refresh(db_gestionaire)
    return db_gestionaire

def get_gestionaire_by_email(db: Session, email: str):
    return db.query(Gestionaire).filter(Gestionaire.email == email).first()