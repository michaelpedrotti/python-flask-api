from flask import Flask
from flask.views import MethodView

def resource(app: Flask, path: str, func: MethodView):
    app.add_url_rule(f"/{path}/<int:id>", strict_slashes=False, view_func=func, methods=["GET", "PUT", "DELETE"])
    app.add_url_rule(f"/{path}/<int:id>/edit", strict_slashes=False, view_func=func, methods=["GET"])
    app.add_url_rule(f"/{path}/new", strict_slashes=False, view_func=func, methods=["GET"])
    app.add_url_rule(f"/{path}", strict_slashes=False, view_func=func, methods=["GET", "POST"])

def route_post(app: Flask, path: str, func):
    app.add_url_rule(path, view_func=func, methods=["POST"])

def route_get(app: Flask, path: str, func):
    app.add_url_rule(path, view_func=func, methods=["GET"])