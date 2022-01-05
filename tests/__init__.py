import pytest
from git_service import create_app
from git_service.common import sql_config
from flask_sqlalchemy import SQLAlchemy


@pytest.fixture
def app():
    app = create_app()
    client = app.test_client()
    app.config.from_object(sql_config.Config)
    db = SQLAlchemy(app)
    with app.app_context():
        # alternative pattern to app.app_context().push()
        # all commands indented under 'with' are run in the app context
        db.create_all()
        yield app
        db.session.remove()  # looks like db.session.close() would work as well
        db.drop_all()