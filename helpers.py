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


def request_square_brackets(form):
    """
    url: https://stackoverflow.com/questions/24808660/sending-a-form-array-to-flask
    """
    data = {}
    for url_k in form:
        v = form[url_k]
        ks = []
        while url_k:
            if '[' in url_k:
                k, r = url_k.split('[', 1)
                ks.append(k)
                if r[0] == ']':
                    ks.append('')
                url_k = r.replace(']', '', 1)
            else:
                ks.append(url_k)
                break
        
        sub_data = data
        
        for i, k in enumerate(ks):
            if k.isdigit():
                k = int(k)
            if i+1 < len(ks):
                if not isinstance(sub_data, dict):
                    break
                if k in sub_data:
                    sub_data = sub_data[k]
                else:
                    sub_data[k] = {}
                    sub_data = sub_data[k]
            else:
                if isinstance(sub_data, dict):
                    sub_data[k] = v

    return data