from flask import request, jsonify
from main import db, bcrypt, app
from app.models.User import User
from app.models.Role import Role
from app.models.Company import Company
from flask import Blueprint
from app.validations.auth_validation import RegisterForm, LoginForm
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from flask_jwt_extended import set_access_cookies, unset_jwt_cookies
import datetime
from sqlalchemy import or_

user_bp = Blueprint('users', __name__, url_prefix='/users')

@user_bp.route('/register', methods=['POST'])
def register_user():
  data = request.form
  form = RegisterForm(data)
  
  with app.app_context():
    if not form.validate():
      return jsonify({"message": "Validation Error", "errors": form.errors}), 400
    
    role = Role.query.filter_by(id=data['role_id']).first()
    company = Company.query.filter_by(company=data['company_name']).first()
    existing_user = User.query.filter(or_(User.username == data['username'].lower(), User.email == data['email'])).first()

    if not company and data['role_id'] != '1':
      return jsonify({"message": "Company does not exist"}), 400

    if existing_user and existing_user.username == data['username'].lower():
      return jsonify({"message": "Username already exists"}), 400
    
    if existing_user and existing_user.email == data['email']:
      return jsonify({"message": "Email already exists"}), 400
    
    if not role:
      return jsonify({"message": "Invalid role id"}), 400
    
    if company and company.company == data['company_name'] and data['role_id'] == '1':
      return jsonify({"message": "Company already has an admin"}), 400

    new_user = User(
      username=data['username'],
      first_name=data['first_name'],
      last_name=data['last_name'],
      email=data['email'],
      role_id=data['role_id'],
      password=bcrypt.generate_password_hash(data['password']),
   )
    db.session.add(new_user)
    db.session.commit()

    if data['role_id'] == '1':
      new_company = Company(company=data['company_name'], admin_id=new_user.id)
      db.session.add(new_company)
      db.session.commit()

      new_user.company_id = new_company.id
      db.session.commit()
    else:
      new_user.company_id = company.id
      db.session.commit()

    
    access_token = create_access_token(identity={"username": data['username'], "id": new_user.id, "company_id": new_user.company_id, "role_id": new_user.role_id}, expires_delta=datetime.timedelta(days=1))
    message = jsonify({"message": "User registered successfully"})
    set_access_cookies(message, access_token)
    return message, 200


@user_bp.route('/login', methods=['POST'])
def login_user():
  data = request.form
  form = LoginForm(data)

  with app.app_context():
    if not form.validate():
      return jsonify({"message": "Validation Error", "errors": form.errors}), 400
    user = User.query.filter_by(email=data['email']).first()
    if not user:
      return jsonify({"message": "Invalid email"}), 400

    if not bcrypt.check_password_hash(user.password, data['password']):
      return jsonify({"message": "Invalid password"}), 400

    access_token = create_access_token(identity={"username": user.username, "id": user.id, "company_id": user.company_id, "role_id": user.role_id}, expires_delta=datetime.timedelta(days=1))
    message = jsonify({"message": "User logged in successfully"})
    set_access_cookies(message, access_token)
    return message, 200

@user_bp.route('/logout', methods=['POST'])  
@jwt_required()
def logout():
  message = jsonify({"message": "User Logged out successfully"})
  unset_jwt_cookies(message)
  return message, 200

@user_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user():
    current_user = get_jwt_identity()
    with app.app_context():
      user = User.query.join(Company, User.company_id == Company.id).join(Role, User.role_id == Role.id).add_columns(Company.company, Role.role).filter(User.id == current_user['id']).first()
      current_user['company_name'] = str(user[1])
      current_user['role_name'] = str(user[2])
      current_user['first_name'] = user[0].to_dict()['first_name']
      current_user['last_name'] = user[0].to_dict()['last_name']
    return jsonify(logged_in_as=current_user), 200