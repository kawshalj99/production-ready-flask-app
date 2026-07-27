from flask import Flask
from app.routes import main
from app.health import health


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    app.register_blueprint(health)

    return app