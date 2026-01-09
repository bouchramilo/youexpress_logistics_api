from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import IntegrityError
from app.routers import zone_router, livreur_router, colis_router, destinataire, historique_router, gestionaire
from app.routers import client_router
from app.core.database import engine, Base
from app.models import Client, Colis, Destinataire, Livreur, Zone, HistoriqueStatut
from app.core.logging_config import get_logger
from app.core.middleware import logging_middleware
from app.core.exceptions import BusinessException

# Initialiser le logger
logger = get_logger("main")

Base.metadata.create_all(bind=engine)
logger.info("Base de données initialisée")

app = FastAPI(title="YouExpress Logistics API", version="1.0.0")

# Ajouter le middleware de logging
app.middleware("http")(logging_middleware)

app.include_router(client_router.router)
app.include_router(zone_router.router)
app.include_router(livreur_router.router)
app.include_router(historique_router.router)
app.include_router(colis_router.router)
app.include_router(destinataire.router)
app.include_router(gestionaire.router, prefix="/gestionaires", tags=["gestionaires"])

logger.info("Tous les routers ont été enregistrés")


@app.get("/")
def read_root():
    logger.debug("Requête GET / - Racine API")
    return {"message": "Welcome to YouExpress Logistics API"}

@app.get("/health")
def health_check():
    logger.debug("Requête GET /health - Vérification de santé")
    return {"status": "healthy"}


# Exception Handlers
@app.exception_handler(BusinessException)
def business_exception_handler(request: Request, exc: BusinessException):
    logger.warning(f"Business exception: {exc.message}")
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": exc.message}
    )

@app.exception_handler(IntegrityError)
def integrity_exception_handler(request: Request, exc: IntegrityError):
    logger.error(f"Database integrity error: {exc.orig}")
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Database integrity error: " + str(exc.orig)}
    )

@app.exception_handler(Exception)
def general_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unexpected error: {exc}")
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content={"detail": "An unexpected error occurred: " + str(exc)}
    )
