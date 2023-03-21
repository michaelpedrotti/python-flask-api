from app import db
from sqlalchemy import Column, Integer, String, JSON


class PermissionModel(db.Model):

    __tablename__ = 'permission'
    
    """ 
    @url https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/  
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    profile_id = Column(Integer, nullable=False)
    resource = Column(String, unique=True, nullable=False)
    actions = Column(JSON)
    

    def __repr__(self):
        return '<Permission %r>' % self.resource

    @property
    def serialize(self):
       return {
           'id': self.id,
           'profile_id': self.profile_id,
           'resource': self.resource,
           'actions': self.actions,
       }