from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from helpers import resource

db = SQLAlchemy()
ma = Marshmallow()

def create_app():

    from views.user import UserView
    from views.profile import ProfileView
    import views.public as public

    app = Flask(__name__)
    app.config.from_pyfile('settings.py')
 
    db.init_app(app)
    ma.init_app(app)

    # https://flask.palletsprojects.com/en/2.2.x/views/
    resource(app, 'user', UserView.as_view('user'))
    resource(app, 'profile', ProfileView.as_view('profile'))

    app.add_url_rule('/', view_func=public.index)

    return app