from flask_sqlalchemy import SQLAlchemy
from main import db
import datetime

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(20), nullable=False)
  last_name = db.Column(db.String(40), nullable=False)
  username = db.Column(db.String(12), nullable=False, unique=True)
  password = db.Column(db.String(120), nullable=False)
  email = db.Column(db.String(120), nullable=False, unique=True)
  created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

  def __repr__(self):
    return f"Username: {self.username}, First Name: {self.first_name}, Last Name: {self.last_name}, Email: {self.email}"
