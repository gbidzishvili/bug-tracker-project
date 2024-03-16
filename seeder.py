from app.models.Role import Role
from main import db, app

def seed_roles():
  with app.app_context():
    Role.query.delete()
    roles = [
      Role(role='Admin'),
      Role(role='Product Manager'),
      Role(role='Developer'),
      Role(role='Tester'),
    ]
    db.session.add_all(roles)
    db.session.commit()
    db.session.close()