from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from app import db


class UserModel(db.Model):

    __tablename__ = 'user'
    
    """ 
    @url https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/  
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(length=255), unique=True, nullable=False)
    name = Column(String(length=100), nullable=False)
    password = Column(String(length=255), nullable=False)
    profile_id = Column(Integer, nullable=False)
    createdAt = Column(DateTime, nullable=False, default=datetime.now())
    updatedAt = Column(DateTime, nullable=False, default=datetime.now())

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