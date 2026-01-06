from pydantic import BaseModel
from typing import Optional

class ZoneBase(BaseModel):
    nom: str
    ville: str
    code_postal: Optional[str] = None
    
class ZoneCreate(ZoneBase):
    pass

class ZoneUpdate(BaseModel):
    nom: Optional[str] = None
    ville: Optional[str] = None
    code_postal: Optional[str] = None
    
class Zone(ZoneBase):
    id: int
    
    class Config:
        from_attributes = True