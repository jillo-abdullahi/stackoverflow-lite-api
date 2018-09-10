# app/__init__.py

from flask import Flask, render_template

from .v1.views.auth import auth
from .v1.views.questions import questions
from .v1.views.answers import answers
from instance.config import app_config


def create_app(config_name):
    """Function to initialize app"""

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.url_map.strict_slashes = False

    # Register our blueprints
    app.register_blueprint(auth)
    app.register_blueprint(questions)
    app.register_blueprint(answers)

    @app.route('/', methods=['GET'])
    @app.route('/favicon.ico', methods=['GET'])
    def api_documentation():
        """route for API documentation"""
        return render_template('version1.html')

    return app
