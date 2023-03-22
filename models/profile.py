from app import db
from sqlalchemy import Column, Integer, String

class Profile(db.Model):

    __tablename__ = 'profile'

    """ 
    @url https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/  
    """
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(length=100), nullable=False)
    # createAt = Column(DateTime, nullable=False)
    # updateAt = Column(DateTime, nullable=False)

    def __repr__(self):
        return '<Profile %r>' % self.id

    @property
    def serialize(self):
       return {
           'id': self.id,
           'name': self.name,
       }
       