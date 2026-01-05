from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Destinataire(Base):
    __tablename__ = "destinataires"

    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False, index=True)
    prenom = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, unique=True, index=True)
    telephone = Column(String, nullable=False)
    adresse = Column(String, nullable=False)


    colis_recus = relationship("Colis", back_populates="destinataire")