from flask import Flask


def init_app():
    """
    Create Flask application
    """
    app = Flask(__name__, instance_relative_config=False, static_folder='static')
    app.config.from_object("config.DevelopmentConfig")

    with app.app_context():
        # Import parts of our application
        from .members import routes as member

        # Register Blueprints
        app.register_blueprint(member.member_bp)

        return app
