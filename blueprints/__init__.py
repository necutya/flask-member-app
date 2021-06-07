"""Initialize Flask app."""
from flask import Flask


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.DevelopmentConfig")

    with app.app_context():
        # Import parts of our application
        from .blueprint import routes as blueprint

        # Register Blueprints
        app.register_blueprint(blueprint.basic_bp)

        return app
