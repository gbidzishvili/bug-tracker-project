from flask import jsonify
from main import app
from app.models.Role import Role
from flask import Blueprint
from flask_jwt_extended import jwt_required


role_bp = Blueprint('roles', __name__, url_prefix='/roles')

@role_bp.route('/get', methods=['GET'])
@jwt_required()
def get_roles():
  with app.app_context():
    roles = Role.query.all()
    return jsonify(roles=[role.__repr__() for role in roles])