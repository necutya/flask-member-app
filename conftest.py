import pytest
from app import app as flask_app

flask_app.config.from_object("config.TestingConfig")


@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()
