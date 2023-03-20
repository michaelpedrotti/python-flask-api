from helpers import request_square_brackets
from flask_sqlalchemy.model import Model
from sqlalchemy.orm.attributes import InstrumentedAttribute


class BaseService():

    def filter(self, dict: dict = {}, model: Model = None, query = None):

        params = request_square_brackets(dict)
        filter: list = []

        if 'field' in params:
            for key in params['field']:
                attr = getattr(model, key)
                if(isinstance(attr, InstrumentedAttribute)):
                    filter.append(attr.contains(params['field'][key])) 

        return query.filter(*filter)   
    
    def find():
        return {}

    def create():
        return {}

    def update():
        return {}

    def delete():
        return {}

    def paginate():
        return {"total": 0, "rows": []}