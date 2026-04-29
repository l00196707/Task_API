from flask import Blueprint, jsonify, current_app

health_bp = Blueprint("health", __name__, url_prefix="/health")

@health_bp.route("")
def health():
    current_app.logger.info("Health check called")
    return jsonify({'status': 'healthy'}), 200
