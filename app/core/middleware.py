import time
from fastapi import Request
from app.core.logging_config import get_logger

logger = get_logger("middleware")

async def logging_middleware(request: Request, call_next):
    """Middleware pour enregistrer toutes les requêtes HTTP"""
    
    start_time = time.time()
    
    # Enregistrer les détails de la requête
    logger.debug(
        f"Requête reçue - Méthode: {request.method}, "
        f"URL: {request.url.path}, "
        f"Client: {request.client.host if request.client else 'Inconnu'}"
    )
    
    try:
        response = await call_next(request)
        process_time = time.time() - start_time
        
        # Enregistrer la réponse
        logger.info(
            f"Requête traitée - Méthode: {request.method}, "
            f"URL: {request.url.path}, "
            f"Statut: {response.status_code}, "
            f"Temps: {process_time:.3f}s"
        )
        
        response.headers["X-Process-Time"] = str(process_time)
        return response
        
    except Exception as e:
        process_time = time.time() - start_time
        logger.error(
            f"Erreur lors du traitement - Méthode: {request.method}, "
            f"URL: {request.url.path}, "
            f"Erreur: {str(e)}, "
            f"Temps: {process_time:.3f}s"
        )
        raise
