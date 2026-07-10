import logging
from flask import Flask, request
from app.health.routes import health_bp
from app.metrics.metrics import REQUEST_COUNT
from app.tasks.routes import tasks_bp
from app.metrics.routes import metrics_bp


def create_app():

    app = Flask(__name__)

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )

    @app.before_request
    def log_request():
        app.logger.info("%s %s", request.method, request.url_rule.rule)

    @app.after_request
    def record_metrics(response):
        endpoint = request.url_rule.rule if request.url_rule else "not_found"
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=endpoint,
            status=response.status_code,
        ).inc()

        return response

    app.register_blueprint(health_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(metrics_bp)

    return app
