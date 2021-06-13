"""Class-based Flask app configuration."""
from os import environ, path

from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, ".env"))


class Config(object):
    """
    Configuration base, for all environments.
    """
    DEBUG = False
    TESTING = False

    SECRET_KEY = environ.get("SECRET_KEY")

    CSRF_ENABLED = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    DATABASE_URI = environ.get("SQLALCHEMY_DATABASE_URI")

    # Static Assets
    STATIC_FOLDER = "static"
    TEMPLATES_FOLDER = "templates"


class ProductionConfig(Config):
    """
    Configuration for production
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(Config):
    """
    Configuration for development
    """
    DEBUG = True


class TestingConfig(Config):
    """
    Configuration for testing
    """
    TESTING = True
    WTF_CSRF_ENABLED = False
