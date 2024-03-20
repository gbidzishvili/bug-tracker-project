from flask import request, jsonify
from main import app, db
from app.models.Project import Project
from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required

project_bp = Blueprint('projects', __name__, url_prefix='/projects')

@project_bp.route('/get', methods=['GET'])
@jwt_required()
def get_projects():
  current_user = get_jwt_identity()
  with app.app_context():
    projects = Project.query.filter_by(company_id = current_user["company_id"]).all()
    projects = [project.toDict() for project in projects]
    return jsonify({"data": projects})
  
@project_bp.route('/create', methods=['POST'])
@jwt_required()
def post_project():
  data = request.form
  current_user = get_jwt_identity()

  if current_user['role_id'] != 1 and current_user['role_id'] != 2:
    return jsonify({"message": "Unauthorized"}), 401

  with app.app_context():
    project = Project(project=data['project'], company_id=current_user['company_id'])
    db.session.add(project)
    db.session.commit()
    return jsonify({"message": "Project created successfully"})