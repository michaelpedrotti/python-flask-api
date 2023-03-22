from flask_sqlalchemy.query import Query
from werkzeug.wrappers.request import ImmutableMultiDict
from .base import BaseService
from . profile import ProfileService
from models.user import UserModel
from app import db
from helpers.password import password_generator
from helpers.model import model_fill
from datetime import datetime
from pprint import pprint


class UserService(BaseService):
    
    def find(self, id = 0, includes = False) -> dict:

        model = UserModel.query.get(id)

        if not model:
            raise Exception('User was not found')

        row: dict =  model.serialize
    
        if includes is not False:
            row["profile"] = ProfileService().find(model.profile_id, True)

        return row


    def create(self, data = {}) -> dict:

        password, data['password'] = password_generator()

        row = UserModel(**data)
        
        db.session.add(row)
        db.session.commit()
        db.session.refresh(row)
        
        return row.serialize

    def update(self, id = 0, data = {}) -> dict:

        row = UserModel.query.get(id)
          
        if not row:
            raise Exception('User was not found')

        model_fill(row, data)

        row.updatedAt = datetime.now()

        db.session.merge(row)
        db.session.commit()

        return row.serialize

    def delete(self, id = 0) -> dict:

        row = UserModel.query.get(id)
          
        if not row:
            raise Exception('User was not found')
        
        db.session.delete(row)
        db.session.commit()

        return row.serialize

    def paginate(self, filter: ImmutableMultiDict) -> dict:

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