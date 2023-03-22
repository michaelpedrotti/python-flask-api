from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from helpers import resource

db = SQLAlchemy()
ma = Marshmallow()

def create_app():

    from views.user import UserView
    from views.profile import ProfileView
    from views.auth import AuthView
    import views.public as public

    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
 
    db.init_app(app)
    ma.init_app(app)

    # https://flask.palletsprojects.com/en/2.2.x/views/
    resource(app, 'user', UserView.as_view('user'))
    resource(app, 'profile', ProfileView.as_view('profile'))

    app.add_url_rule('/auth/login', view_func=AuthView.login, methods=["POST"])
    app.add_url_rule('/auth/me', view_func=AuthView.my_self, methods=["GET"])
    app.add_url_rule('/auth/setting', view_func=AuthView.set_auth_setting, methods=["POST"])
    app.add_url_rule('/auth/setting', view_func=AuthView.get_auth_setting, methods=["GET"])
    
    app.add_url_rule('/', view_func=public.index)

    return app