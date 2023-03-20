from functools import wraps
from flask import request, jsonify, g, current_app, globals
from services.authentication import Authentication
from services.user import UserService
from pprint import pprint

def is_authenticated(wrapped):
    """
    url: https://flask.palletsprojects.com/en/2.2.x/patterns/viewdecorators/
    """
    @wraps(wrapped)
    def decorated_function(*args, **kwargs):

        json = {"error": False}

        try:

            header = request.headers.get('authorization')

            if header is None:
                raise Exception('No Authorization header was sent')

            token = header.replace("Bearer ", "")

            data: dict = Authentication().verify(token)

            g.user: dict = UserService().find(data.get("id"))

            return wrapped(*args, **kwargs)

        except Exception as e:
            json["message"] = str(e)
            return jsonify(json), 401
        
    return decorated_function