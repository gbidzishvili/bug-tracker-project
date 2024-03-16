from main import db
import datetime

class Role(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  role = db.Column(db.String(50), nullable=False, unique=True)
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)
  
  def __repr__(self):
    return self.role
