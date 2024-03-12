from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class RegisterForm(FlaskForm):
    first_name = StringField('first_name', [validators.Length(min=2, max=20)])
    last_name = StringField('last_name', [validators.Length(min=2, max=40)])
    username = StringField('username', [validators.Length(min=4, max=12)])
    email = StringField('email', [validators.Length(min=6, max=50)])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('confirm_password', message='Passwords do not match'),
        validators.Length(min=8, max=40)
    ])
    confirm_password = PasswordField('confirm_password')