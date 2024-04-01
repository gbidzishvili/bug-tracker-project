from flask_seeder import Seeder
from app.models.Status import Status

class SeedStatus(Seeder):
  def run(self):
    Status.query.delete()
    status = [
      Status(status='New', description='Has just been reported.'),
      Status(status='WIP', description='Work in progress by a developer.'),
      Status(status='Resolved', description='Developer believes bug is fixed.'),
      Status(status='Reopened', description="Last resolution wasn't successful."),
      Status(status='Closed', description="Tester verifies the last resolution.")
    ]
    self.db.session.add_all(status)
    self.db.session.commit()
    self.db.session.close()
    print("Added Status!")
