from datetime import datetime
from app import db


class UserModel(db.Model):

    __tablename__ = 'user'
    
    """ 
    @url https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/  
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    profile_id = db.Column(db.Integer, nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.now())
    updatedAt = db.Column(db.DateTime, nullable=False, default=datetime.now())

    def __repr__(self):
        return '<User %r>' % self.email

    @property
    def serialize(self):
       return {
           'id': self.id,
           'email': self.email,
           'name': self.name,
           'profile_id': self.profile_id,
           'createdAt': datetime.strftime(self.createdAt, '%Y-%m-%d %H:%M:%S'),
           'updatedAt': datetime.strftime(self.updatedAt, '%Y-%m-%d %H:%M:%S')
       }