from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base


class Client(Base):
    __tablename__ = "clients"
    id = Column(Integer, primary_key=True, index=True) 
    nom = Column(String, nullable=False, index=True)
    prenom = Column(String, nullable=False, index=True)
    email = Column(String, nullable=False, index=True)
    adresse = Column(String, nullable=False, index=True)
    telephone = Column(String, nullable=False, index=True)
    ville = Column(String, nullable=False, index=True)
    colis = relationship("Colis", back_populates="client")  
