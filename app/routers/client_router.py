from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.services.client_service import create_client
from app.schemas.client import ClientCreate, ClientResponse
from app.core.database import get_db

router = APIRouter(prefix="/clients", tags=["clients"])

@router.post("/", response_model=ClientResponse)
def create_new_client(client: ClientCreate, db: Session = Depends(get_db)):
    return create_client(db=db, client=client)