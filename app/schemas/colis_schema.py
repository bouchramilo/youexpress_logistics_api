from pydantic import BaseModel
from typing import Optional


from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime

class ColisCreate(BaseModel):  
    client_id: int 
    description: str
    poids: float
    statut: str = "CREE"
    ville_destination: str
    client_id: int
    destinataire_id: int

class ColisResponse(BaseModel):
    id: int
    description: Optional[str]
    poids: float
    statut: str
    ville_destination: str
    date_creation: datetime
    client_id: int
    destinataire_id: int
    zone_id: Optional[int] = None
    livreur_id: Optional[int] = None

    model_config = ConfigDict(from_attributes=True)

class ColisUpdate(BaseModel):
    statut: Optional[str] = None
    zone_id: Optional[int] = None
    livreur_id: Optional[int] = None

class ColisAssign(BaseModel):
    livreur_id: int