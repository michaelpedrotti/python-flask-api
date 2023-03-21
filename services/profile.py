from flask_sqlalchemy.query import Query
from werkzeug.wrappers.request import ImmutableMultiDict
from .base import BaseService
from models.profile import Profile
from app import db
# from pprint import pprint


class ProfileService(BaseService):
    """ url https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/ """
    
    def find(self, id = 0) -> dict:

        row = Profile.query.get(id)

        if not row:
            raise Exception('Profile was not found')

        return row.serialize

    def create(self, data = {}) -> dict:
        """ url: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists """
        row = Profile(**data)
        
        db.session.add(row)
        db.session.commit()
        db.session.refresh(row)
        
        return row.serialize

    def update(self, id = 0, data = {}) -> dict:

        row = Profile.query.get(id)
          
        if not row:
            raise Exception('Profile was not found')
    
        row.name = data["name"]

        db.session.merge(row)
        db.session.commit()

        return row.serialize

    def delete(self, id = 0) -> dict:

        row = Profile.query.get(id)
          
        if not row:
            raise Exception('Profile was not found')
        
        db.session.delete(row)
        db.session.commit()

        return row.serialize

    def paginate(self, filter: ImmutableMultiDict) -> dict:
        """ 
        url: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/pagination/ 
        url: https://stackoverflow.com/questions/20642497/sqlalchemy-query-to-return-only-n-results
        """
        
        query: Query = Profile.query

        query = self.filter(filter.to_dict(), Profile, query)

        total = query.count()       

        offset = int(filter.get('offset', 0))
        limit = int(filter.get('limit', 10))

        query = query.offset(offset).limit(limit)

        return {
            "total": total,
            "rows": [ row.serialize for row in query.all() ]
        }