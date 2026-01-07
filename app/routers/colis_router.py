from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.colis_service import create_colis
from app.schemas.colis_schema import ColisCreate, ColisResponse , ColisUpdate
from app.core.database import get_db

router = APIRouter(prefix='/colis' , tags=['colis'])

@router.post('/')
def create_colis(colis : create_colis , db : Session = Depends(get_db) ):
    return create_colis(db = db ,  colis = colis)