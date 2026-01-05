# youexpress_logistics_api
YouLogiX — Plateforme de gestion logistique en temps réel destinée à YouExpress, basée sur un backend moderne développé avec FastAPI, SQLAlchemy et Pydantic. La solution est conçue pour assurer la scalabilité, une validation rigoureuse des données et une maintenance durable à long terme.

## Configuration

1. Copiez le fichier `.env.example` vers `.env` et ajustez les variables d'environnement selon vos besoins.

2. Assurez-vous que Docker et Docker Compose sont installés et en cours d'exécution.

## Lancement avec Docker

Pour lancer l'application en mode développement avec Docker :

```bash
docker-compose up --build
```

L'API sera accessible sur `http://localhost:8000`.

La base de données PostgreSQL sera accessible sur `localhost:5432`.

## Documentation API

Une fois l'application lancée, la documentation Swagger est disponible sur `http://localhost:8000/docs`.

## Tests

Pour exécuter les tests :

```bash
docker-compose exec app pytest
```

## Structure du projet

- `app/`: Code de l'application
  - `main.py`: Point d'entrée FastAPI
  - `core/`: Configuration et base de données
  - `models/`: Modèles SQLAlchemy
  - `schemas/`: Schémas Pydantic
  - `routers/`: Routes FastAPI
  - `services/`: Logique métier
- `requirements.txt`: Dépendances Python
- `Dockerfile`: Configuration Docker pour l'application
- `docker-compose.yml`: Orchestration des services
- `.env`: Variables d'environnement (non versionné)
