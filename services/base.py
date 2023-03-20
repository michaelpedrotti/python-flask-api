from helpers import request_square_brackets
from flask_sqlalchemy.model import Model
from sqlalchemy.orm.attributes import InstrumentedAttribute
from sqlalchemy.sql.elements import ColumnElement
from pprint import pprint
import re



class BaseService():

    def filter(self, dict: dict = {}, model: Model = None, query = None):

        params = request_square_brackets(dict)
        filter: list = []

        if 'field' in params:
            for key in params['field']:
                
                val = params['field'][key]
                
                if(str(key).find('.') > -1):
                          
                    name, action = str(key).split('.')

                    attr = getattr(model, name)
                    if(isinstance(attr, InstrumentedAttribute)):

                        column: ColumnElement = None

                        match action:
                            case "like": column = attr.contains(val)
                            case "notLike": column = attr.not_like("%{}%".format(val))
                            case "startsWith": column = attr.startswith(val)
                            case "endSwith": column = attr.endswith(val)
                            case "notIn": column = attr.not_in(val)
                            case "in": column = attr.in_(re.split(r'[\s\;\,\|]+', val))
                            case _: column = attr.__eq__(val)

                        filter.append(column)       
                else:
                    attr = getattr(model, key)
                    if(isinstance(attr, InstrumentedAttribute)):
                        filter.append(attr.__eq__(val)) 
 

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