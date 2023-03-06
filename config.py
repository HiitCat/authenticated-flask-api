import os

class Config:
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') or 'jwt-secret-key'
    JWT_TOKEN_LOCATION = os.environ.get('JWT_TOKEN_LOCATION') or 'headers'
    JWT_HEADER_NAME = os.environ.get('JWT_HEADER_NAME') or 'Authorization'
    JWT_HEADER_TYPE = os.environ.get('JWT_HEADER_TYPE') or 'Bearer'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
