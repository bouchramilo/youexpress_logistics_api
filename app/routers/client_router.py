from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from app.services.client_service import create_client, get_all_clients, get_client_by_id
from app.schemas.client import ClientCreate, ClientResponse
from app.core.database import get_db

router = APIRouter(prefix="/clients", tags=["clients"])

@router.post("/", response_model=ClientResponse)
def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db=db, client=client)

@router.get("/", response_model=List[ClientResponse])
def get_clients(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_all_clients(db=db, skip=skip, limit=limit)

@router.get("/{client_id}", response_model=ClientResponse)
def get_client(client_id: int, db: Session = Depends(get_db)):
    return get_client_by_id(db=db, client_id=client_id)