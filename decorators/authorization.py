from functools import wraps
# from flask import g, Response

def is_authorized(wrapped):
    """
    url: https://flask.palletsprojects.com/en/2.2.x/patterns/viewdecorators/
    """
    def decorated_function(*args, **kwargs):
        # return Response('{"error": true}', 403)
        return wrapped(*args, **kwargs)
    return decorated_function