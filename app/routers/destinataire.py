from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.services.destinataire_service import create_destinataire, get_all_destinataires, get_destinataire_by_id
from app.schemas.destinataire import DestinataireCreate, DestinataireResponse
from app.core.database import get_db

router = APIRouter(prefix='/destinataires', tags=['destinataires'])

@router.post('/', response_model=DestinataireResponse)
def create_dest(destinataire: DestinataireCreate, db: Session = Depends(get_db)):
    return create_destinataire(db=db, destinataire=destinataire)

@router.get('/', response_model=List[DestinataireResponse])
def get_destinataires(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_destinataires(db=db, skip=skip, limit=limit)

@router.get('/{destinataire_id}', response_model=DestinataireResponse)
def get_destinataire(destinataire_id: int, db: Session = Depends(get_db)):
    return get_destinataire_by_id(db=db, destinataire_id=destinataire_id)
