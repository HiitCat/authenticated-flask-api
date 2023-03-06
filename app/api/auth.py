import jwt
from app import app
from app.models import User
from flask import jsonify, request
from datetime import datetime, timedelta

@app.route('/api/authenticate', methods=['POST'])
def authenticate():
    username = request.json.get('username')
    password = request.json.get('password')
    # Vérification de l'authentification de l'utilisateur
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        # Création du token JWT avec une expiration de 30 minutes
        token_payload = {'sub': { 'id': user.id, 'username': user.username}, 'exp': datetime.utcnow() + timedelta(minutes=30)}
        token = jwt.encode(token_payload, app.config['JWT_SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token}), 200
    else:
        return jsonify({'message': 'Identifiant ou mot de passe incorrect'}), 401
