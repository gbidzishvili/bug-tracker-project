from flask_seeder import Seeder
from app.models.Role import Role
from sqlalchemy.sql import text

class SeedStatus(Seeder):
  def run(self):
    self.db.session.execute(text('set foreign_key_checks = 0'))
    self.db.session.execute(text('truncate table role'))
    roles = [
      Role(role='Admin'),
      Role(role='Product Manager'),
      Role(role='Developer'),
      Role(role='Tester'),
    ]
    self.db.session.add_all(roles)
    self.db.session.commit()
    self.db.session.close()
    self.db.session.execute(text('set foreign_key_checks = 1'))
    print("Added Roles!")