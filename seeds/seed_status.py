from flask_seeder import Seeder
from app.models.Status import Status

class SeedStatus(Seeder):
  def run(self):
    Status.query.delete()
    status = [
      Status(status='New'),
      Status(status='WIP'),
      Status(status='Resolved'),
      Status(status='Reopened'),
      Status(status='Closed')
    ]
    self.db.session.add_all(status)
    self.db.session.commit()
    self.db.session.close()
    print("Added Status!")
