from flask import Flask

def create_app():
    app = Flask(__name__)

    from app.health.routes import health_bp
    from app.tasks.routes import tasks_bp

    app.register_blueprint(health_bp)
    app.register_blueprint(tasks_bp)

    return app
