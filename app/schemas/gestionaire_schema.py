from pydantic import BaseModel, EmailStr, ConfigDict

class GestionaireCreate(BaseModel):
    nom: str
    email: EmailStr
    mot_de_passe: str

class GestionaireResponse(BaseModel):
    id: int
    nom: str
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)