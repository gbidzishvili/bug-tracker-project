from flask import request, jsonify
from main import db, bcrypt, app
from app.models.User import User
from flask import Blueprint
from app.validations.auth_validation import RegisterForm, LoginForm
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_jwt_extended import set_access_cookies, unset_jwt_cookies
import datetime

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

    access_token = create_access_token(identity=data['username'], expires_delta=datetime.timedelta(minutes=1440))
    message = jsonify({"message": "User registered successfully"})
    set_access_cookies(message, access_token)

    return message, 200


@user_bp.route('/login', methods=['POST'])
def login_user():
  data = request.form
  form = LoginForm(data)

  if not form.validate():
    return jsonify({"message": "Validation Error", "errors": form.errors}), 400

  with app.app_context():
    user = User.query.filter_by(email=data['email']).first()
    if not user:
      return jsonify({"message": "Invalid email"}), 400

    if not bcrypt.check_password_hash(user.password, data['password']):
      return jsonify({"message": "Invalid password"}), 400

    access_token = create_access_token(identity=user.username, expires_delta=datetime.timedelta(minutes=1440))
    message = jsonify({"message": "User Logged in successfully"})
    set_access_cookies(message, access_token)
    return message, 200

@user_bp.route('/logout', methods=['POST'])  
@jwt_required()
def logout():
  message = jsonify({"message": "User Logged out successfully"})
  unset_jwt_cookies(message)
  return message, 200

@user_bp.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200