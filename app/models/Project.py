from main import db
import datetime

class Project(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  project = db.Column(db.String(100), nullable=False)
  company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)
  
  def toDict(self):
    return {
      'id': self.id,
      'project': self.project,
      'company_id': self.company_id,
    }