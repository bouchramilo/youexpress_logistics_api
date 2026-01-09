# Système de Logging - YouExpress Logistics API

## Vue d'ensemble

Un système de logging complet a été implémenté pour journaliser toutes les actions et événements applicatifs. Ce système utilise le module `logging` standard de Python avec plusieurs handlers pour enregistrer les événements à différents niveaux.

## Architecture du Logging

### 1. Configuration Centralisée (`app/core/logging_config.py`)

Le fichier `logging_config.py` configure le système de logging avec:

- **Format de log**: `%(asctime)s - %(name)s - %(levelname)s - [%(filename)s:%(lineno)d] - %(message)s`
- **Répertoire des logs**: `logs/` (créé automatiquement)
- **Niveaux de log**: DEBUG, INFO, WARNING, ERROR

### 2. Handlers

#### Handler Fichier (Tous les logs)
- **Fichier**: `logs/app_YYYYMMDD.log`
- **Niveau**: DEBUG
- **Taille max**: 10 MB
- **Backups**: 10 fichiers de rotation

#### Handler Erreurs
- **Fichier**: `logs/error_YYYYMMDD.log`
- **Niveau**: ERROR
- **Taille max**: 10 MB
- **Backups**: 10 fichiers de rotation

#### Handler Console
- **Niveau**: INFO
- **Affichage**: En temps réel dans la console

## Utilisation du Logger

### Obtenir un logger dans un module:

```python
from app.core.logging_config import get_logger

logger = get_logger("module_name")
```

### Enregistrer des événements:

```python
# Informations (événements importants)
logger.info(f"Colis créé avec succès (ID: {colis.id})")

# Débogage (informations détaillées)
logger.debug(f"Validation réussie pour le colis {colis_id}")

# Avertissements (situations inhabituelles)
logger.warning(f"Tentative d'accès à un colis inexistant (ID: {colis_id})")

# Erreurs (problèmes graves)
logger.error(f"Erreur lors de la création du colis: {str(e)}")
```

## Middleware HTTP

Le fichier `app/core/middleware.py` contient un middleware qui enregistre automatiquement:

- **Toutes les requêtes reçues**: Méthode, URL, Client IP
- **Toutes les réponses**: Statut HTTP, temps de traitement
- **Les erreurs**: Exceptions avec contexte

### Exemple de log du middleware:

```
2026-01-08 14:23:45 - youexpress.middleware - INFO - Requête traitée - Méthode: POST, URL: /colis/1/historiques, Statut: 201, Temps: 0.045s
```

## Modules avec Logging Intégré

### 1. Service Historique (`app/services/historique_service.py`)

```python
logger.info(f"Création d'un nouvel historique pour le colis {colis_id}")
logger.debug(f"Dernier statut trouvé: '{ancien_statut}' - Transition vers '{nouveau_statut}'")
```

### 2. Service Colis (`app/services/colis_service.py`)

```python
logger.info(f"Création d'un nouveau colis - Description: {description}")
logger.info(f"Colis créé avec succès (ID: {colis_id})")
logger.debug(f"Création automatique de l'historique initial")
```

### 3. Router Historique (`app/routers/historique_router.py`)

```python
logger.info(f"Demande de création d'historique pour le colis {colis_id}")
logger.warning(f"Tentative de création d'historique pour un colis inexistant")
logger.debug(f"Validation réussie")
```

### 4. Application principale (`app/main.py`)

```python
logger.info("Base de données initialisée")
logger.info("Tous les routers ont été enregistrés")
```

## Structure des Fichiers de Log

### logs/app_20260108.log
```
2026-01-08 13:45:23 - youexpress.main - INFO - Base de données initialisée
2026-01-08 13:45:23 - youexpress.main - INFO - Tous les routers ont été enregistrés
2026-01-08 13:45:45 - youexpress.colis_service - INFO - Création d'un nouveau colis - Description: Test Colis, Poids: 2.5kg, Statut: PENDING
2026-01-08 13:45:45 - youexpress.colis_service - INFO - Colis créé avec succès (ID: 1) - Client: 1, Destinataire: 1
2026-01-08 13:45:46 - youexpress.historique_router - INFO - Demande de création d'historique pour le colis 1
2026-01-08 13:45:46 - youexpress.historique_service - INFO - Création d'un nouvel historique pour le colis 1 avec le statut 'EN_STOCK'
```

### logs/error_20260108.log
```
2026-01-08 14:02:33 - youexpress.historique_router - WARNING - Tentative de création d'historique pour un colis inexistant (ID: 999)
2026-01-08 14:02:35 - youexpress.historique_router - WARNING - Tentative de création d'historique avec un livreur inexistant (ID: 999)
```

## Niveaux de Log Recommandés

| Niveau | Utilisation | Exemple |
|--------|-------------|---------|
| **DEBUG** | Informations détaillées pour le débogage | Validation réussie, transition de statut |
| **INFO** | Événements importants | Création de ressources, changements significatifs |
| **WARNING** | Situations inhabituelles mais gérées | Ressource non trouvée, validation échouée |
| **ERROR** | Erreurs graves | Exceptions, échecs de base de données |

## Avantages du Système

✅ **Traçabilité complète**: Tous les événements sont enregistrés avec timestamp
✅ **Débogage facile**: Logs détaillés avec noms de fichiers et numéros de lignes
✅ **Performance**: Les logs ne ralentissent pas l'application
✅ **Rotation automatique**: Les fichiers de log sont gérés automatiquement
✅ **Multiples canaux**: Console + Fichiers (général et erreurs)
✅ **Contexte riche**: Chaque log inclut des informations de contexte

## Accès aux Logs

```bash
# Voir les logs en temps réel
docker compose logs app -f

# Voir les fichiers de log générés
docker compose exec app ls -la logs/

# Afficher le contenu d'un log
docker compose exec app cat logs/app_20260108.log

# Filtrer les erreurs
docker compose exec app grep ERROR logs/app_20260108.log
```
