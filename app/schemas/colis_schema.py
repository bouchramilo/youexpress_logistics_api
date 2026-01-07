from pydantic import BaseModel
from typing import Optional


class ColisCreate(BaseModel):   
    description : str
    poids : float
    statut : str = "CREE"
    ville_destination : str
    date_creation : str
    client_id : int
    destinataire_id : int
    # zone_id : int
    # destinataire_id : int
    # livreur_id : int

class ColisResponse(BaseModel):
    id : int
    description : str
    poids : float
    statut : str
    ville_destination : str
    date_creation : str
    client_id : int
    # zone_id : int
    destinataire_id : int
    # livreur_id : int

    class Config:
        fom_attributes = True

class ColisUpdate(BaseModel):
    statut : Optional[str]
    zone_id : int
    livreur_id : int