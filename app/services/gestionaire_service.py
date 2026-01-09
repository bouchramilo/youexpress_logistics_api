from sqlalchemy.orm import Session
from app.models.gestionaire import Gestionaire  # Make sure this matches your model filename
from app.schemas.gestionaire_schema import GestionaireCreate
from app.core.exceptions import BusinessException

def create_gestionaire(db: Session, gestionaire_data: GestionaireCreate):
    if not gestionaire_data.nom:
        raise BusinessException("INVALID_NAME", "Le nom du gestionnaire est requis")
    
    if not gestionaire_data.email:
        raise BusinessException("INVALID_EMAIL", "L'email du gestionnaire est requis")
    
    if not gestionaire_data.mot_de_passe:
        raise BusinessException("INVALID_PASSWORD", "Le mot de passe du gestionnaire est requis")
    
    existing_gestionaire = db.query(Gestionaire).filter(Gestionaire.email == gestionaire_data.email).first()
    if existing_gestionaire:
        raise BusinessException("EMAIL_ALREADY_EXISTS", f"Un gestionnaire avec l'email {gestionaire_data.email} existe déjà")
    
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