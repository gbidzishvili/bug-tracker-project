from main import db
from app.models.Bug import Bug
import datetime

class Project(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  project = db.Column(db.String(100), nullable=False)
  company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
  bugs = db.relationship(Bug, backref=db.backref('project'))
  created_at = db.Column(db.DateTime, default=datetime.datetime.now)
  
  def to_dict(self):
    return {
      'id': self.id,
      'project': self.project,
      'company_id': self.company_id,
      'bugs_length': len(self.bugs),
      'newest_bug': len(self.bugs) and self.bugs[-1].to_dict()['created_at'],
      'oldest_bug': len(self.bugs) and self.bugs[0].to_dict()['created_at'],
      'statuses': {
        "new": len([bug for bug in self.bugs if bug.status_id == 1]),
        "wip": len([bug for bug in self.bugs if bug.status_id == 2]),
        "resolved": len([bug for bug in self.bugs if bug.status_id == 3]),
        "reopened": len([bug for bug in self.bugs if bug.status_id == 4]),
        "closed": len([bug for bug in self.bugs if bug.status_id == 5])
      },
      "severities": {
        "cosmetic": len([bug for bug in self.bugs if bug.severity_id == 1]),
        "low": len([bug for bug in self.bugs if bug.severity_id == 2]),
        "medium": len([bug for bug in self.bugs if bug.severity_id == 3]),
        "high": len([bug for bug in self.bugs if bug.severity_id == 4]),
        "critical": len([bug for bug in self.bugs if bug.severity_id == 5])
      }
    }