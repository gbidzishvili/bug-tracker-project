from main import db
from app.models.Bug import Bug
import datetime

class Project(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  project = db.Column(db.String(100), nullable=False)
  company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
  bugs = db.relationship(Bug, backref=db.backref('project'))
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)
  
  def to_dict(self, withBugs=False):
    return {
      'id': self.id,
      'project': self.project,
      'company_id': self.company_id,
      'bugs': withBugs == True and [bug.to_dict() for bug in self.bugs]
    }