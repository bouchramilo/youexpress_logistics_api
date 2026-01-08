from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.destinataire_service import create_destinataire 
from app.schemas.destinataire import DestinataireCreate
from app.core.database import get_db

router = APIRouter(prefix='/destinataires' , tags=['colis'])

@router.post('/')
def create_colis(destinataire : DestinataireCreate , db : Session = Depends(get_db) ):
    return create_destinataire(db = db ,  destinataire= destinataire)
