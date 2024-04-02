from main import db
from app.models.Severity import Severity
from app.models.Status import Status
from app.models.User import User
import datetime

class Bug(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), nullable=False)
  description = db.Column(db.Text, nullable=False)
  solution = db.Column(db.Text, nullable=True)
  severity_id = db.Column(db.Integer, db.ForeignKey('severity.id'), nullable=False)
  severity = db.relationship(Severity, backref=db.backref('bug'))
  status_id = db.Column(db.Integer, db.ForeignKey('status.id'), nullable=False)
  status = db.relationship(Status, backref=db.backref('bug'))
  project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
  reporter_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  reporter = db.relationship(User, foreign_keys=[reporter_id], backref=db.backref('reporter'))
  resolver_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
  resolver = db.relationship(User, foreign_keys=[resolver_id], backref=db.backref('resolver'))
  company_id = db.Column(db.Integer, db.ForeignKey('company.id'), nullable=False)
  created_at = db.Column(db.DateTime, default=datetime.datetime.now(datetime.UTC))
  updated_at = db.Column(db.DateTime, default=datetime.datetime.now(datetime.UTC))
  
  def to_dict(self):
    return {
      "name": self.name,
      "description": self.description,
      "solution": self.solution,
      "severity": self.severity.severity,
      "status": self.status.status,
      "project_id": self.project_id,
      "company_id": self.company_id,
      "reporter": {
        "first_name": self.reporter.first_name, 
        "last_name": self.reporter.last_name,
        "username": self.reporter.username,
      },
      "resolver": self.resolver is not None and {
        "first_name": self.resolver.first_name, 
        "last_name": self.resolver.last_name,
        "username": self.resolver.username,
      },
    }
