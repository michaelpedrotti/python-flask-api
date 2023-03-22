from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired

class ProfileValidator(FlaskForm):
    
    """ https://flask-wtf.readthedocs.io/en/1.0.x/quickstart/ """
    class Meta:
        csrf = False

    name = StringField('name', validators=[
        DataRequired()
    ])

    email = StringField('email', validators=[
        DataRequired()
    ])