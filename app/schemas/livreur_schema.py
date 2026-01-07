from pydantic import BaseModel
from typing import Optional

class LivreurBase(BaseModel):
    nom: str
    prenom: str
    telephone: str
    vehicule: str
    zone: str
    
class LivreurCreate(LivreurBase):
    pass

class LivreurUpdate(BaseModel):
    nom: Optional[str] = None
    prenom: Optional[str] = None
    telephone: Optional[str] = None
    vehicule: Optional[str] = None
    zone: Optional[str] = None


class Livreur(LivreurBase):
    id: int
    
    class Config:
        from_attributes = True
        