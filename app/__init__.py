from flask import Flask
from flask_jwt_extended import JWTManager
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config.Config')

jwt = JWTManager(app)

db = SQLAlchemy(app)

from app import views, models

with app.app_context():
    db.drop_all()
    db.create_all()
    user = models.User(username='test', email='test@test.com')
    user.set_password(password='password')
    db.session.add(user)
    db.session.commit()

from app.api import auth