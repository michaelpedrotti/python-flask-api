from functools import wraps
from flask import g, request, jsonify
from services.authorization import AuthorizationService
from pprint import pprint


def is_authorized(wrapped):
    """
    url: https://flask.palletsprojects.com/en/2.2.x/patterns/viewdecorators/
    """
    def decorated_function(*args, **kwargs):

        json = {"error": False}

        try:
            user: dict = g.get('user')

            if user is None:
                raise Exception('Not Autenticated')

            resource = request.view_args['resource']
            action = request.view_args['action']
                
            if AuthorizationService().has_permission(resource, action, user.get('id')) is not True:
                raise Exception('Forbidden')
            
            return wrapped(*args, **kwargs)

        except Exception as e:
            json["message"] = str(e)
            return jsonify(json), 403
        
    return decorated_function