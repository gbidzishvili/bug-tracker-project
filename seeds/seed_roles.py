from flask_seeder import Seeder
from app.models.Role import Role

class SeedStatus(Seeder):
  def run(self):
    Role.query.delete()
    roles = [
      Role(role='Admin'),
      Role(role='Product Manager'),
      Role(role='Developer'),
      Role(role='Tester'),
    ]
    self.db.session.add_all(roles)
    self.db.session.commit()
    self.db.session.close()
    print("Added Roles!")