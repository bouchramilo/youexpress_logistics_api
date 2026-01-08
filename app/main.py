from fastapi import FastAPI
from app.routers import zone_router, livreur_router, colis_router, destinataire, historique_router, gestionaire
from app.routers import client_router
from app.core.database import engine, Base
from app.models import Client, Colis, Destinataire, Livreur, Zone, HistoriqueStatut 

Base.metadata.create_all(bind=engine)

app = FastAPI(title="YouExpress Logistics API", version="1.0.0")

app.include_router(client_router.router)
app.include_router(zone_router.router)
app.include_router(livreur_router.router)
app.include_router(historique_router.router)
app.include_router(colis_router.router)
app.include_router(destinataire.router)
app.include_router(gestionaire.router, prefix="/gestionaires", tags=["gestionaires"])


@app.get("/")
def read_root():
    return {"message": "Welcome to YouExpress Logistics API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}


