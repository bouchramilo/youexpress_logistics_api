from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List, Optional
from app.core.database import get_db
from app.schemas.colis_schema import ColisCreate, ColisResponse, ColisUpdate, ColisAssign
from app.services import colis_service

router = APIRouter(prefix='/colis', tags=['colis'])

@router.post('/', response_model=ColisResponse)
def create_colis_endpoint(colis: ColisCreate, db: Session = Depends(get_db)):
    return colis_service.create_colis(db=db, colis=colis)

@router.get("/", response_model=List[ColisResponse])
def read_colis(
    statut: Optional[str] = Query(None, description="Filtrer par statut"),
    zone_id: Optional[int] = Query(None, description="Filtrer par zone"),
    db: Session = Depends(get_db)
):
    """
    Gestionnaire Story: Consulter la liste de tous les colis et filtrer par statut/zone.
    """
    return colis_service.get_all_colis(db, statut=statut, zone_id=zone_id)


@router.get("/{colis_id}", response_model=ColisResponse)
def read_colis_by_id(colis_id: int, db: Session = Depends(get_db)):
    colis = colis_service.get_colis_by_id(db, colis_id)
    if not colis:
        raise HTTPException(status_code=404, detail="Colis not found")
    return colis


@router.put("/{colis_id}", response_model=ColisResponse)
def update_colis_endpoint(colis_id: int, colis: ColisUpdate, db: Session = Depends(get_db)):
    updated_colis = colis_service.update_colis(db, colis_id, colis)
    if not updated_colis:
        raise HTTPException(status_code=404, detail="Colis not found")
    return updated_colis


@router.patch("/{colis_id}/assign", response_model=ColisResponse)
def assign_livreur_endpoint(colis_id: int, assign_data: ColisAssign, db: Session = Depends(get_db)):
    """
    Gestionnaire Story: Assigner un colis à un livreur.
    """
    colis = colis_service.assign_livreur_to_colis(db, colis_id, assign_data.livreur_id)
    if not colis:
        raise HTTPException(status_code=404, detail="Colis not found")
    return colis