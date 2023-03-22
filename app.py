from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from helpers.route import resource, route_get, route_post

db = SQLAlchemy()
ma = Marshmallow()

def create_app():

    from views.user import UserView
    from views.profile import ProfileView
    from views.auth import AuthView
    from views.public import PublicView

    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
 
    db.init_app(app)
    ma.init_app(app)

    # https://flask.palletsprojects.com/en/2.2.x/views/
    resource(app, 'user', UserView.as_view('user'))
    resource(app, 'profile', ProfileView.as_view('profile'))

    route_post(app, '/auth/login', AuthView.login)
    route_get(app, '/auth/me', AuthView.my_self)

    route_post(app, '/auth/setting', AuthView.set_auth_setting)
    route_get(app, '/auth/setting', AuthView.get_auth_setting)

    route_get(app, '/', PublicView.index)

    return app