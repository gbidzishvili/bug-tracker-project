from main import db
import datetime

class Severity(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  severity = db.Column(db.String(50), nullable=False, unique=True)
  description = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)
  
  def to_dict(self):
    return {"severity_id": self.id, "severity": self.severity, "description": self.description}
