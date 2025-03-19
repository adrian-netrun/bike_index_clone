from flask import Flask
from .src.routes.index import base
from .src.routes.login import rc_login
from .src.routes.register import rc_register
from .db import db_session

from dotenv import load_dotenv

load_dotenv("./dev/.env")


def create_app(test_config=None) -> object:
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    app.register_blueprint(base)
    app.register_blueprint(rc_register)
    app.register_blueprint(rc_login)

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db_session.remove()
        print("session closed")

    shutdown_session()

    return app
