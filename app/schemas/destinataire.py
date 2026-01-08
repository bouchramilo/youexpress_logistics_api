from pydantic import BaseModel, EmailStr

class DestinataireCreate(BaseModel):
    nom: str
    prenom: str
    email: EmailStr
    telephone: str
    adresse: str