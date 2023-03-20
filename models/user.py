from datetime import datetime
from app import db


class UserModel(db.Model):
    """ 
    @url https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/  
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    profile_id = db.Column(db.Integer, nullable=False)
    createAt = db.Column(db.DateTime, nullable=False, default=datetime())
    updateAt = db.Column(db.DateTime, nullable=False, default=datetime())