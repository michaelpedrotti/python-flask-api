from sqlalchemy import sql
from flask_sqlalchemy.pagination import QueryPagination
from flask_sqlalchemy.query import Query
from .base import BaseService
from models.profile import Profile
from app import db
from pprint import pprint


class ProfileService(BaseService):
    """ url https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/ """
    
    def find(self, id = 0):

        row = Profile.query.get(id)

        if not row:
            raise Exception('Profile was not found')

        return row.serialize

    def create(self, data = {}):
        """ url: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists """
        row = Profile(**data)
        
        db.session.add(row)
        db.session.commit()
        
        return row.serialize

    def update(self, id = 0, data = {}):

        row = Profile.query.get(id)
          
        if not row:
            raise Exception('Profile was not found')
    
        row.name = data["name"]

        db.session.merge(row)
        db.session.commit()

        return row.serialize

    def delete(self, id = 0):

        row = Profile.query.get(id)
          
        if not row:
            raise Exception('Profile was not found')
        
        db.session.delete(row)
        db.session.commit()

        return row.serialize

    def paginate(self, filter = {}):
        """ url: https://flask-sqlalchemy.palletsprojects.com/en/3.0.x/pagination/ """
        
        # query: sql.Select = db.select(Profile) \
        #     .order_by(Profile.id) \
        #     .limit(5) \
        #     .offset(0)

        # paginator: Pagination = db.paginate(query)

        query: Query = Profile.query

        paginator: QueryPagination = query.paginate(per_page=5, page=2)

        pprint(Profile.query)
        # pprint(queryP.total)
        # pprint(queryP.items)
        # flask_sqlalchemy.pagination.QueryPagination

        # [ pprint(row) for row in paginator ]
        # 
        return {
            "meta": {
                "first": paginator.first,
                "last": paginator.last

            },
            "total": paginator.total,
            "rows": [ row.serialize for row in paginator.items ]
        }