from flask_sqlalchemy.query import Query
from werkzeug.wrappers.request import ImmutableMultiDict
from .base import BaseService
from models.permssion import PermissionModel
from app import db
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql.elements import ColumnElement
from helpers import passwordGenerator
from pprint import pprint


class PermissionService(BaseService):
    
    def find(self, id = 0) -> dict:

        model = PermissionModel.query.get(id)

        if not model:
            raise Exception('User was not found')

        return model.serialize
    
    def all(*, filter: dict = {}) -> tuple:
        
        model = PermissionModel
        query = PermissionModel.query
        kargs = []
        
        for name, value in filter.items():
            
            attr = getattr(model, name)
            if(isinstance(attr, InstrumentedAttribute)):
                
                column: ColumnElement = None

                if(isinstance(value, dict)):

                    for key, val in value.items():

                        pprint("if: " + key + " = " + str(val))

                        match key:
                            case "contains": column = attr.contains(val)
                            case "not_like": column = attr.not_like(val)
                            case "startswith": column = attr.startswith(val)
                            case "endswith": column = attr.endswith(val)
                            case "not_in": column = attr.not_in(val)
                            case "in": column = attr.in_(val)
                            case _: column = attr.__eq__(val)

                else:
                    pprint("else: " + name + " = " + str(value))
                    column = attr.__eq__(value)


                kargs.append(column) 

        query = query.filter(*kargs)

        return query.all()


    def create(self, data = {}) -> dict:

        row = PermissionModel(**data)
        
        db.session.add(row)
        db.session.commit()
        db.session.refresh(row)
        
        return row.serialize

    def update(self, id = 0, data = {}) -> dict:

        row = PermissionModel.query.get(id)
          
        if not row:
            raise Exception('User was not found')
    
        row.profile_id = data["profile_id"]
        row.resource = data["resource"]
        row.actions = data["actions"]

        db.session.merge(row)
        db.session.commit()

        return row.serialize

    def delete(self, id = 0) -> dict:

        row = PermissionModel.query.get(id)
          
        if not row:
            raise Exception('User was not found')
        
        db.session.delete(row)
        db.session.commit()

        return row.serialize

    def paginate(self, filter: ImmutableMultiDict) -> dict:

        query: Query = PermissionModel.query
        
        query = self.filter(filter.to_dict(), PermissionModel, query)

        total = query.count()       

        offset = int(filter.get('offset', 0))
        limit = int(filter.get('limit', 10))

        query = query.offset(offset).limit(limit)

        return {
            "total": total,
            "rows": [ row.serialize for row in query.all() ]
        }