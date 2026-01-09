from pydantic import BaseModel, EmailStr, ConfigDict

class DestinataireCreate(BaseModel):
    nom: str
    prenom: str
    email: EmailStr
    telephone: str
    adresse: str

class DestinataireResponse(BaseModel):
    id: int
    nom: str
    prenom: str
    email: EmailStr
    telephone: str
    adresse: str
    
    model_config = ConfigDict(from_attributes=True)