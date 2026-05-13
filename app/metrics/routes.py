from flask import Blueprint, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST

metrics_bp = Blueprint("metrics", __name__, url_prefix="/metrics")

@metrics_bp.route("", methods=["GET"], strict_slashes=False)
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)
