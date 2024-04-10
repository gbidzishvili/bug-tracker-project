from flask import jsonify
from main import app
from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required
from app.models.Status import Status

status_bp = Blueprint('status', __name__, url_prefix='/status')

@status_bp.route('/get', methods=['GET'])
@jwt_required()
def get_severities():
  with app.app_context():
    statuses = Status.query.all()
    statuses = [status.to_dict() for status in statuses]
    return jsonify({"data": statuses})

