# app/__init__.py

from flask import Flask

from .v1.views.auth import auth
from .v1.views.questions import questions
from instance.config import app_config


def create_app(config_name):
    """Function to initialize app"""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False

    # Register our blueprints
    app.register_blueprint(auth)
    app.register_blueprint(questions)

    return app
