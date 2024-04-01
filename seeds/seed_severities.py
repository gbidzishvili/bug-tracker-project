from flask_seeder import Seeder
from app.models.Severity import Severity

class SeedSeverities(Seeder):
  def run(self):
    Severity.query.delete()
    severities = [
      Severity(severity='Cosmetic', description='Visual bug, no impact on functionality.'),
      Severity(severity='Low', description='Minor impact on functionality.'),
      Severity(severity='Medium', description="Causes unexpected behavior, but doesn't break the software."),
      Severity(severity='High', description='Severely hinders functionality, or results in significant data corruption.'),
      Severity(severity='Critical', description='Causes a complete system crash, making it unusable.')
    ]
    self.db.session.add_all(severities)
    self.db.session.commit()
    self.db.session.close()
    print("Added Severities!")