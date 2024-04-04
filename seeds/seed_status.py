from flask_seeder import Seeder
from app.models.Status import Status
from sqlalchemy.sql import text

class SeedStatus(Seeder):
  def run(self):
    self.db.session.execute(text('set foreign_key_checks = 0'))
    self.db.session.execute(text('truncate table status'))
    status = [
      Status(status='New', color='#e04c2b', description='Has just been reported.'),
      Status(status='WIP', color='#6554AF', description='Work in progress by a developer.'),
      Status(status='Resolved', color='#08D9D6', description='Developer believes bug is fixed.'),
      Status(status='Reopened', color='#FF2E63', description="Last resolution wasn't successful."),
      Status(status='Closed', color='#32CD32', description="Tester verifies the last resolution.")
    ]
    self.db.session.add_all(status)
    self.db.session.commit()
    self.db.session.close()
    self.db.session.execute(text('set foreign_key_checks = 1'))
    print("Added Status!")
