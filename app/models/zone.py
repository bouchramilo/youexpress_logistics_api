from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.core.database import Base

class Zone(Base):
    __tablename__ = "zones"
    
    id = Column(Integer, primary_key=True, index=True)
    nom = Column(String, nullable=False, index=True)
    ville = Column(String, nullable=False, index=True)
    code_postal = Column(String, nullable=True)
    colis = relationship("Colis", back_populates="zone")
