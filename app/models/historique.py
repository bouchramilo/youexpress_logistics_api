from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.sql import func
from app.core.database import Base

class HistoriqueStatut(Base):
    __tablename__ = "historique_statuts"

    id = Column(Integer, primary_key=True, index=True)
    
    ancien_statut = Column(String, nullable=True)
    nouveau_statut = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    colis_id = Column(Integer, ForeignKey("colis.id"), nullable=False)
    livreur_id = Column(Integer, ForeignKey("livreurs.id"), nullable=True)