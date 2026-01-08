from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.gestionaire_schema import GestionaireCreate, GestionaireResponse
from app.services import gestionaire_service # Make sure this import matches the filename

router = APIRouter()

@router.post("/", response_model=GestionaireResponse, status_code=201)
def create_gestionaire_endpoint(gestionaire_data: GestionaireCreate, db: Session = Depends(get_db)):
    existing_user = gestionaire_service.get_gestionaire_by_email(db, email=gestionaire_data.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return gestionaire_service.create_gestionaire(db, gestionaire_data)