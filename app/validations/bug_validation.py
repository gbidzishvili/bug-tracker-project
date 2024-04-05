from flask_wtf import FlaskForm
from wtforms import StringField, validators, IntegerField

class PostBug(FlaskForm):
  name = StringField('name', [
    validators.DataRequired(),
    validators.Length(min=3, max=30, message='Name must be between 3 and 30'),
    validators.Regexp('^[a-zA-Z0-9 ]+$', message='Enter only symbols')
  ])
  description = StringField('description', [
    validators.DataRequired(),
    validators.Length(min=100, max=1000, message='Description must be between 100 and 1000'),
  ])
  severity_id = IntegerField('severity_id', [validators.DataRequired()])
  project_id = IntegerField('project_id', [validators.DataRequired()])