from flask import Flask
from views.user import UserView
from views.profile import ProfileView
import views.public as public
from helpers import resource

app = Flask(__name__)
app.config.from_pyfile('settings.py')

# https://flask.palletsprojects.com/en/2.2.x/views/
resource(app, 'user', UserView.as_view('user'))
resource(app, 'profile', ProfileView.as_view('profile'))

app.add_url_rule('/', view_func=public.index)


if __name__ == '__main__':
    app.run(debug=True)