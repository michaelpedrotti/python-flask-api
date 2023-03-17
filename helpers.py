def resource(app, path, func):
    app.add_url_rule(f"/{path}/<int:id>", view_func=func, methods=["GET", "PUT", "DELETE"])
    app.add_url_rule(f"/{path}/<int:id>/edit", view_func=func, methods=["GET"])
    app.add_url_rule(f"/{path}/new", view_func=func, methods=["GET"])
    app.add_url_rule(f"/{path}", view_func=func, methods=["GET", "POST"])