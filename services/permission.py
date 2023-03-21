from flask_sqlalchemy.query import Query
from sqlalchemy.sql.elements import ColumnElement
from sqlalchemy.orm import Query
from werkzeug.wrappers.request import ImmutableMultiDict
from models.permssion import PermissionModel
from .base import BaseService
from app import db
from pprint import pprint


class PermissionService(BaseService):
    
    def find(self, id = 0) -> dict:

        model = PermissionModel.query.get(id)

        if not model:
            raise Exception('User was not found')

        return model.serialize
    
    def all(self, filter: dict = {}, columns: tuple = []) -> tuple:
        
        model = PermissionModel
        query: Query = PermissionModel.query
        kargs = []

        for name, value in filter.items():
            
            attr = self.find_model_column(model, name)
            if(attr is not None):
                
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
                    column = attr.__eq__(value)

                kargs.append(column) 

        query = query.filter(*kargs)

        # if len(columns) > 0:
        #     columns = [self.find_model_column(model, column) for column in columns if column is not None ]
        # query = query.with_entities(PermissionModel.resource)
        # lost serialize property

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