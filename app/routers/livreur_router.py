from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.livreur_schema import Livreur, LivreurCreate, LivreurUpdate
from app.services import livreur_service

router = APIRouter(prefix="/livreurs", tags=["livreurs"])

@router.post("/", response_model=Livreur, status_code=status.HTTP_201_CREATED)
def create_livreurs(livreur: LivreurCreate, db: Session = Depends(get_db)):
    return livreur_service.create_livreur(db=db, livreur=livreur)


@router.get("/", response_model=List[Livreur])
def read_livreurs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return livreur_service.index_livreurs(db, skip=skip, limit=limit)


@router.get("/{livreur_id}", response_model=Livreur)
def read_livreur(livreur_id: int, db: Session = Depends(get_db)):
    db_liveur = livreur_service.show_livreur(db, livreur_id)
    if db_liveur is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Livreur non trouvé")
    return db_liveur