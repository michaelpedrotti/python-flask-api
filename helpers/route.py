from flask import Flask
from flask.views import MethodView


def route_resource(app: Flask, resource: str, func: MethodView):

    resources = [
        ['index',   'GET',    f'/{resource}',               'read'  ],
        ['create',  'GET',    f'/{resource}/new',           'create'],
        ['store',   'POST',   f'/{resource}',               'create'],
        ['show',    'GET',    f'/{resource}/<int:id>',      'read'  ],
        ['edit',    'GET',    f'/{resource}/<int:id>/edit', 'update'],
        ['update',  'PUT',    f'/{resource}/<int:id>',      'update'],
        ['destroy', 'DELETE', f'/{resource}/<int:id>',      'delete'],
    ]

    for [ name, method, path, action ] in resources:
        
        app.add_url_rule(path.format(resource=resource), 
            strict_slashes=False, 
            view_func=func, 
            methods=[ method ], 
            defaults={'resource': resource, 'action': action}
        )

def route_post(app: Flask, path: str, func):
    
    app.add_url_rule(path, 
        strict_slashes=False, 
        view_func=func, 
        methods=["POST"]
    )

def route_get(app: Flask, path: str, func):

    app.add_url_rule(path, 
        strict_slashes=False, 
        view_func=func, 
        methods=["GET"]
    )