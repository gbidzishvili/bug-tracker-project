from flask import request, jsonify
from main import db, bcrypt, app
from app.models.User import User
from flask import Blueprint
from app.validations.auth_validation import RegisterForm
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/register', methods=['POST'])
def register_user():
  data = request.form
  form = RegisterForm(data)
  if not form.validate():
    return jsonify({"message": "Validation Error", "errors": form.errors}), 400
  
  with app.app_context():
    if User.query.filter_by(username=data['username']).first():
      return jsonify({"message": "Username already exists"}), 400
    
    if User.query.filter_by(email=data['email']).first():
      return jsonify({"message": "Email already exists"}), 400

  new_user = User(
      username=data['username'],
      first_name=data['first_name'],
      last_name=data['last_name'],
      email=data['email'],
      password=bcrypt.generate_password_hash(data['password'])
  )
  with app.app_context():
    db.session.add(new_user)
    db.session.commit()

  access_token = create_access_token(identity=data['username'])
  return jsonify({"message": "User registered successfully", "access_token": access_token}), 201


@user_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200