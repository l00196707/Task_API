from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__, url_prefix="/health")

@health_bp.route("")
def health():
    return jsonify({'status': 'healthy'}), 200
