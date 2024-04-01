from main import db
import datetime

class Status(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  status = db.Column(db.String(50), nullable=False, unique=True)
  description = db.Column(db.String(255), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)
  
  def to_dict(self):
    return {"status_id": self.id, "status": self.status, "description": self.description}
