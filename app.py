from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from helpers.route import route_resource, route_get, route_post

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    """ factory function  """

    from views.user import UserView
    from views.profile import ProfileView
    from views.auth import AuthView
    from views.public import PublicView

    app = Flask(__name__)
    app.config.from_object('settings')
 
    db.init_app(app)
    migrate.init_app(app, db)

    # https://flask.palletsprojects.com/en/2.2.x/views/
    route_resource(app, 'user', UserView.as_view('user'))
    route_resource(app, 'profile', ProfileView.as_view('profile'))

    route_post(app, '/auth/login', AuthView.login)
    route_get(app, '/auth/me', AuthView.my_self)

    route_post(app, '/auth/setting', AuthView.set_auth_setting)
    route_get(app, '/auth/setting', AuthView.get_auth_setting)

    route_get(app, '/', PublicView.index)

    return app