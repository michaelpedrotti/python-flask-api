from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Email

class UserValidator(FlaskForm):
    
    class Meta:
        csrf = False

    name = StringField('name', validators=[
        DataRequired()
    ])

    email = EmailField('email', validators=[
        DataRequired()
    ])