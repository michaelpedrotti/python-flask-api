from flask_sqlalchemy.query import Query
from werkzeug.wrappers.request import ImmutableMultiDict
from .base import BaseService
from .permission import PermissionService
from models.profile import Profile
from app import db
from pprint import pprint


class ProfileService(BaseService):
    """ url https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/ """
    
    def find(self, id = 0, includes = False) -> dict:

        model = Profile.query.get(id)

        if not model:
            raise Exception('Profile was not found')

        row: dict = model.serialize

        if includes is not False:
            rows = PermissionService().all({"profile_id": model.id}, ['resource', 'actions'])
            row["permissions"] = [ row.serialize for row in rows ]

        return row

    def create(self, data: dict = {}) -> dict:
        """ url: https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists """

        row = Profile(name=data.get('name'))
        
        db.session.add(row)
        db.session.commit()
        db.session.refresh(row)

        if data.get('permissions') is not None:
            
            service = PermissionService()
            
            for resource, actions in data.get('permissions').items():

                service.create({
                    'resource': resource,
                    'actions': actions,
                    'profile_id': row.id,
                })
        
        return row.serialize

    def update(self, id = 0, data: dict = {}) -> dict:

        row = Profile.query.get(id)
          
        if not row:
            raise Exception('Profile was not found')
    
        row.name = data.get("name")

        db.session.merge(row)
        db.session.commit()

        if data.get('permissions') is not None:
            
            service = PermissionService()

            deleted: tuple = service.all({
                "profile_id": row.id,
                "resource": {
                    "not_in": data.get('permissions').keys()
                }
            })

            if len(deleted) > 0:
                for row in deleted:
                    # .delete({id: row.id, profile: model.id});
                    service.delete(id)

            saved = { row["resource"]: row["id"] for row in service.all({
                "profile_id": row.id,
                "resource": {
                    "in": data.get('permissions').keys()
                }
            })}

            for resource, actions in data.get('permissions').items():
                
                if(resource in saved):
                    id = saved.get(resource)
                    
                    service.update({
                        'resource': resource,
                        'actions': actions,
                        'profile_id': row.id,
                    }, id)
                else:
                    service.create({
                        'resource': resource,
                        'actions': actions,
                        'profile_id': row.id,
                    })        

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