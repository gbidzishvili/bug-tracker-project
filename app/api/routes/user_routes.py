from flask import request, jsonify
from main import db, bcrypt, app
from app.models.User import User
from flask import Blueprint

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/register', methods=['POST'])
def register_user():
  data = request.get_json()
  new_user = User(
      id=1,
      username=data['username'],
      first_name=data['first_name'],
      last_name=data['last_name'],
      email=data['email'],
      password=bcrypt.generate_password_hash(data['password'])
  )
  with app.app_context():
    db.session.add(new_user)
    db.session.commit()
  return jsonify({"message": "User registered successfully"}), 201