from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators


class RegisterForm(FlaskForm):
    first_name = StringField('first_name', [
        validators.DataRequired(),
        validators.Length(min=2, max=20, message='Name must be between 2 and 20'),
        validators.Regexp('^[a-zA-Z]+$', message='Enter only letters')
    ])
    last_name = StringField('last_name', [
        validators.DataRequired(),
        validators.Length(min=2, max=40, message='Surname must be between 2 and 40'),
        validators.Regexp('^[a-zA-Z]+$', message='Enter only letters')
    ])
    username = StringField('username', [
        validators.DataRequired(),
        validators.Length(min=4, max=12, message='Username must be between 4 and 12'),
        validators.Regexp('^[a-zA-Z0-9!-)]+$', message="Such symbol isn't allowed!")
    ])
    email = StringField('email', [
        validators.DataRequired(),
        validators.Length(min=4, max=50),
        validators.Email(message='Invalid email format')
    ])
    password = PasswordField('password', [
        validators.DataRequired(),
        validators.EqualTo('confirm_password', message='Passwords do not match'),
        validators.Length(min=8, max=40)
    ])
    confirm_password = PasswordField('confirm_password')
    role_id = StringField('role_id', [
        validators.DataRequired(),
        validators.Regexp('^[1-4]+$', message='Enter only numbers'),
    ])
    company_name = StringField('company_name', [
        validators.DataRequired(),
        validators.Length(min=3, max=30, message='Must be between 3 and 20'),
        validators.Regexp('^[a-zA-Z0-9 ]+$', message='Letters and numbers only')
    ])

class LoginForm(FlaskForm):
    email = StringField('email', [
        validators.DataRequired(),
        validators.Length(min=4, max=50),
        validators.Email(message='Invalid email format')
    ])
    password = PasswordField('password', [validators.DataRequired(),  validators.Length(min=8, max=40)])