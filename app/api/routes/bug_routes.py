from flask import request, jsonify
from main import app, db
from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.validations.bug_validation import PostBug
from app.models.Bug import Bug
from app.models.Project import Project

bug_bp = Blueprint('bugs', __name__, url_prefix='/bugs')

@bug_bp.route('/get/<project_id>', methods=['GET'])
@jwt_required()
def get_bugs(project_id):
  current_user = get_jwt_identity()
  with app.app_context():
    bugs = Bug.query.filter_by(project_id = project_id, company_id=current_user['company_id']).all()
    bugs = [bug.to_dict() for bug in bugs]
    return jsonify({"data": bugs})

@bug_bp.route('/create', methods=['POST'])
@jwt_required()
def post_bug():
  data = request.form
  form = PostBug(data)
  current_user = get_jwt_identity()

  if not form.validate():
      return jsonify({"message": "Validation Error", "errors": form.errors}), 400

  with app.app_context():
    project = Project.query.filter_by(id = data['project_id']).first()
    if not project:
      return jsonify({"message": "Project not found"}), 404
    if project.company_id != current_user['company_id']:
      return jsonify({"message": "You are not authorized to create a bug for this project"}), 401
    
    bug = Bug(**data, status_id = 1, company_id = current_user['company_id'], reporter_id = current_user['id'])
    db.session.add(bug)
    db.session.commit()
    return jsonify({"message": "Bug created successfully"})