from flask import Flask

def create_app():
    app = Flask(__name__)
    
    from app.health.routes import health_bp
    
    app.register_blueprint(health_bp)

    return app