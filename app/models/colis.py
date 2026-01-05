from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Colis(Base):
    __tablename__ = "colis"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, nullable=True)
    poids = Column(Float, nullable=False)
    statut = Column(String, default="CREE", index=True)
    ville_destination = Column(String, nullable=False)
    date_creation = Column(DateTime(timezone=True), server_default=func.now())
    client_id = Column(Integer, ForeignKey("clients.id"), nullable=False)
    zone_id = Column(Integer, ForeignKey("zones.id"), nullable=False)
    destinataire_id = Column(Integer, ForeignKey("destinataires.id"), nullable=False)
    livreur_id = Column(Integer, ForeignKey("livreurs.id"), nullable=True)
    client = relationship("Client", back_populates="colis")
    zone = relationship("Zone", back_populates="colis")
    destinataire = relationship("Destinataire", back_populates="colis_recus")
    livreur = relationship("Livreur", back_populates="colis_assignes")