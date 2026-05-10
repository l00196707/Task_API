import logging
from flask import Flask, request
from app.health.routes import health_bp
from app.tasks.routes import tasks_bp

def create_app():

    app = Flask(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s %(levelname)s %(message)s"
    )

    @app.before_request
    def log_request():
        app.logger.info("%s %s", request.method, request.path)



    app.register_blueprint(health_bp)
    app.register_blueprint(tasks_bp)

    return app
