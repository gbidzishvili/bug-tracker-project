from main import db
import datetime

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(20), nullable=False)
  last_name = db.Column(db.String(40), nullable=False)
  username = db.Column(db.String(12), nullable=False, unique=True)
  password = db.Column(db.String(120), nullable=False)
  email = db.Column(db.String(120), nullable=False, unique=True)
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)
  role_id = db.Column(db.Integer, db.ForeignKey('role.id'), nullable=False)
  company_name = db.Column(db.String(40), nullable=False, unique=True)

  def __repr__(self):
    return {"username": self.username, "first_name": self.first_name, "last_name": self.last_name, "email": self.email, "role_id": self.role_id, "company_name": self.company_name}
