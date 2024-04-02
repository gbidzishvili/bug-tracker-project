from flask_wtf import FlaskForm
from wtforms import StringField, validators


class PostProject(FlaskForm):
  project = StringField('project', [
    validators.DataRequired(),
    validators.Length(min=3, max=30, message='Title must be between 3 and 30'),
    validators.Regexp('^[a-zA-Z0-9 ]+$', message="Such symbol isn't allowed!")
  ])