from functools import wraps
from flask import g, Response

def is_authenticated(wrapped):
    """
    url: https://flask.palletsprojects.com/en/2.2.x/patterns/viewdecorators/
    """
    @wraps(wrapped)
    def decorated_function(*args, **kwargs):
        if g.get('user') is None:
            return Response('{"error": true}', 401)
        return wrapped(*args, **kwargs)
    return decorated_function