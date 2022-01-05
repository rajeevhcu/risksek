import syslog
from flask import Flask, jsonify
from flask_api import status
from flask_swagger_ui import get_swaggerui_blueprint
from flask_sqlalchemy import SQLAlchemy

from git_service.common.error_response import error_response_preparation
from .common import constants, sql_config, log

global db


def page_not_found(e):
    # note that we set the 404 status explicitly
    response = error_response_preparation(
        404,
        constants.CLIENT_ERROR,
        "Page Not Found"
    )
    return jsonify(response, status.HTTP_404_NOT_FOUND)


def internal_server_error(e):
    # note that we set the 500 status explicitly
    response = error_response_preparation(
        500,
        constants.RESPONSE_ERROR,
        "Internal Server Error"
    )
    return response, status.HTTP_500_INTERNAL_SERVER_ERROR


def create_app():
    """ to create and configure the flask application."""
    try:
        app = Flask(__name__, instance_relative_config=True)
        # CORS(app)
        # swagger specific
        SWAGGER_URL = '/swagger'
        API_URL = '/static/swagger.yml'
        SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
            SWAGGER_URL,
            API_URL,
            config={
                'app_name': "git_service"
            }
        )
        # end swagger specific
        app.url_map.strict_slashes = False

        app.config.from_object(sql_config.Config)
        global db
        db = SQLAlchemy(app)

        app.register_error_handler(404, page_not_found)
        app.register_error_handler(500, internal_server_error)
        app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)

        from .controller import organization
        app.register_blueprint(organization.bp)

        @app.route("/")
        def home():
            return """<h1> Welcome to Git Service </h1>"""

        @app.teardown_request
        def session_clear(exception=None):
            db.session.remove()
            if exception and db.session.is_active:
                log.info("rollback the session")
                db.session.rollback()

        return app
    except Exception as err:
        syslog.syslog('Error in git services create_app :' + str(err))
        raise err
