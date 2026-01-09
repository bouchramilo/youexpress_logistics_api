from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class HistoriqueBase(BaseModel):
    ancien_statut: Optional[str] = None
    nouveau_statut: str
    timestamp: Optional[datetime] = None
    colis_id: int
    livreur_id: Optional[int] = None


class HistoriqueCreate(BaseModel):
    nouveau_statut: str
    livreur_id: Optional[int] = None


class Historique(HistoriqueBase):
    id: int

    class Config:
        from_attributes = True


class HistoriqueUpdate(BaseModel):
    ancien_statut: Optional[str] = None
    nouveau_statut: Optional[str] = None
    timestamp: Optional[datetime] = None
    colis_id: Optional[int] = None
    livreur_id: Optional[int] = None
    