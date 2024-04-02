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
    bug = Bug(**data, company_id = current_user['company_id'])
    db.session.add(bug)
    db.session.commit()
    return jsonify({"message": "Bug created successfully"})