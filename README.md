# Authenticated Flask API

Ce projet est une API Flask qui permet de gérer l'authentification et les autorisations d'utilisateurs avec JSON Web Token (JWT).

## Installation

1. Cloner le projet depuis GitHub : `git clone https://github.com/mxcezl/authenticated-flask-api.git`
2. Accéder au dossier : `cd authenticated-flask-api`
3. Installer les dépendances : `pip install -r requirements.txt`

## Configuration

Le fichier `api/config.py` contient les variables d'environnement nécessaires pour l'application.

## Utilisation

1. Lancer l'application : `python run.py`
2. Accéder à l'API depuis l'adresse `http://localhost:5000/api/`

### Endpoints

- `/api/authenticate` : endpoint pour l'authentification des utilisateurs. Requiert une requête POST avec des informations d'identification valides. Retourne un token JWT valide.
- `/api/secret` : endpoint qui nécessite un token JWT valide pour y accéder. Retourne un message de confirmation si l'utilisateur est authentifié.

## License

Ce projet est sous la licence MIT.
