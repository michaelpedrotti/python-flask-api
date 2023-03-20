def resource(app, path, func):
    app.add_url_rule(f"/{path}/<int:id>", strict_slashes=False, view_func=func, methods=["GET", "PUT", "DELETE"])
    app.add_url_rule(f"/{path}/<int:id>/edit", strict_slashes=False, view_func=func, methods=["GET"])
    app.add_url_rule(f"/{path}/new", strict_slashes=False, view_func=func, methods=["GET"])
    app.add_url_rule(f"/{path}", strict_slashes=False, view_func=func, methods=["GET", "POST"])

def get_body(request):
    return (
        request.get_json(force=True, silent=True)
        or
        request.form.to_dict()
    )