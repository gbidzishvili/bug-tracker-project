from main import db
from app.models.Role import Role
from app.models.Company import Company
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
  role = db.relationship(Role, backref=db.backref('user'))
  company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=True)
  company = db.relationship(Company, foreign_keys=[company_id], backref=db.backref('user'))
  # reporter = db.relationship('Bug', backref='reporter')
  # resolver = db.relationship('Bug', backref='resolver')
  def to_dict(self):
    return {
      "username": self.username, 
      "first_name": self.first_name, 
      "last_name": self.last_name, 
      "email": self.email, "role_id": self.role_id, 
      "company_id": self.company_id,
      "role": self.role.role,
      "company": self.company.company
    }
