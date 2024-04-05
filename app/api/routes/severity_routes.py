from flask import request, jsonify
from main import app, db
from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models.Severity import Severity

severity_bp = Blueprint('severities', __name__, url_prefix='/severities')

@severity_bp.route('/get', methods=['GET'])
@jwt_required()
def get_severities():
  with app.app_context():
    severities = Severity.query.all()
    severities = [severity.to_dict() for severity in severities]
    return jsonify({"data": severities})

