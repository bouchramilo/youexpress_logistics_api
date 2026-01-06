from pydantic import BaseModel


class ClientCreate(BaseModel):
    nom: str
    prenom: str
    email: str
    adresse: str
    telephone: str
    ville: str


class ClientResponse(BaseModel):
    id: int
    nom: str
    prenom: str
    email: str
    adresse: str
    telephone: str
    ville: str

    class Config:
        from_attributes = True

