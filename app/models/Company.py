from main import db
import datetime

class Company(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  company = db.Column(db.String(50), nullable=False, unique=True)
  admin_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  admin = db.relationship('User', foreign_keys=[admin_id], backref=db.backref('admin'))
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)


