from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class Gestionaire(Base):
    __tablename__ = "gestionaires"
    id = Column(Integer , primary_key=True , index=True)
    nom = Column(String , nullable=False)
    email = Column(String , unique=True , index=True , nullable=False)
    mot_de_passe = Column(String , nullable=False)