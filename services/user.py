from flask_sqlalchemy.query import Query
from werkzeug.wrappers.request import ImmutableMultiDict
from .base import BaseService
from models.user import UserModel
from app import db
from helpers import passwordGenerator
from pprint import pprint


class UserService(BaseService):
    
    def find(self, id = 0):

        row = UserModel.query.get(id)

        if not row:
            raise Exception('User was not found')

        return row.serialize

    def create(self, data = {}):

        data['password'] = passwordGenerator()

        pprint(data)

        row = UserModel(**data)
        
        db.session.add(row)
        db.session.commit()
        db.session.refresh(row)
        
        return row.serialize

    def update(self, id = 0, data = {}):

        row = UserModel.query.get(id)
          
        if not row:
            raise Exception('User was not found')
    
        row.name = data["name"]

        db.session.merge(row)
        db.session.commit()

        return row.serialize

    def delete(self, id = 0):

        row = UserModel.query.get(id)
          
        if not row:
            raise Exception('User was not found')
        
        db.session.delete(row)
        db.session.commit()

        return row.serialize

    def paginate(self, filter: ImmutableMultiDict):

        query: Query = UserModel.query

        query = self.filter(filter.to_dict(), UserModel, query)

        total = query.count()       

        offset = int(filter.get('offset', 0))
        limit = int(filter.get('limit', 10))

        query = query.offset(offset).limit(limit)

        return {
            "total": total,
            "rows": [ row.serialize for row in query.all() ]
        }