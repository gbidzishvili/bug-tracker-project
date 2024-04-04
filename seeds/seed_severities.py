from flask_seeder import Seeder
from app.models.Severity import Severity
from sqlalchemy.sql import text

class SeedSeverities(Seeder):
  def run(self):
    self.db.session.execute(text('set foreign_key_checks = 0'))
    self.db.session.execute(text('truncate table severity'))
    severities = [
      Severity(severity='Cosmetic', color="#6554AF", description='Visual bug, no impact on functionality.'),
      Severity(severity='Low', color="#08D9D6", description='Minor impact on functionality.'),
      Severity(severity='Medium', color="#32CD32", description="Causes unexpected behavior, but doesn't break the software."),
      Severity(severity='High', color="#e04c2b", description='Severely hinders functionality, or results in significant data corruption.'),
      Severity(severity='Critical', color="#FF2E63", description='Causes a complete system crash, making it unusable.')
    ] 
    self.db.session.add_all(severities)
    self.db.session.commit()
    self.db.session.close()
    self.db.session.execute(text('set foreign_key_checks = 1'))
    print("Added Severities!")