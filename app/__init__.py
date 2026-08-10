import logging
import time
from flask import Flask, request, g
from app.health.routes import health_bp
from app.metrics.metrics import REQUEST_COUNT, REQUEST_LATENCY
from app.tasks.routes import tasks_bp
from app.metrics.routes import metrics_bp


def create_app():

    app = Flask(__name__)

    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s"
    )

    @app.before_request
    def log_request():
        g.start_time = time.perf_counter()
        g.endpoint = request.url_rule.rule if request.url_rule else "not_found"
        app.logger.info("%s %s", request.method, g.endpoint)

    @app.after_request
    def record_metrics(response):
        duration = time.perf_counter() - g.start_time
        REQUEST_COUNT.labels(
            method=request.method,
            endpoint=g.endpoint,
            status=response.status_code,
        ).inc()

        REQUEST_LATENCY.labels(
            method=request.method,
            endpoint=g.endpoint,
        ).observe(duration)

        return response

    app.register_blueprint(health_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(metrics_bp)

    return app
