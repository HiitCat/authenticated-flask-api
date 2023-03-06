from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import jsonify, request
from app import app

@app.route('/api/secret')
@jwt_required()
def secret():
    current_user = get_jwt_identity()
    username = current_user.get("username")
    return jsonify({'message': f'Vous êtes connecté en tant que {username} !'})
