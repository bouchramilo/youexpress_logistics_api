import logging
import logging.handlers
from pathlib import Path
from datetime import datetime

# Créer le répertoire de logs s'il n'existe pas
LOGS_DIR = Path("logs")
LOGS_DIR.mkdir(exist_ok=True)

# Configuration des noms de fichiers de logs
LOG_FILE = LOGS_DIR / f"app_{datetime.now().strftime('%Y%m%d')}.log"
ERROR_LOG_FILE = LOGS_DIR / f"error_{datetime.now().strftime('%Y%m%d')}.log"

def setup_logging():
    """Configure le système de logging pour l'application"""
    
    # Format des logs
    log_format = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Configuration du logger principal
    logger = logging.getLogger("youexpress")
    logger.setLevel(logging.DEBUG)
    
    # Handler pour les fichiers (tous les logs)
    file_handler = logging.handlers.RotatingFileHandler(
        LOG_FILE,
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=10,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)
    
    # Handler pour les erreurs (erreurs seulement)
    error_handler = logging.handlers.RotatingFileHandler(
        ERROR_LOG_FILE,
        maxBytes=10 * 1024 * 1024,  # 10 MB
        backupCount=10,
        encoding='utf-8'
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(log_format)
    logger.addHandler(error_handler)
    
    # Handler pour la console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)
    
    return logger

# Initialiser le logger au moment de l'import
logger = setup_logging()

def get_logger(name: str):
    """Obtenir un logger avec un nom spécifique"""
    return logging.getLogger(f"youexpress.{name}")
