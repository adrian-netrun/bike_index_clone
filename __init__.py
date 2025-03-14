from flask import Flask

from .src.routes.index import base
from .src.routes.login import rc_login
from .src.routes.register import rc_register
from .src.error_handler import bp

from dotenv import load_dotenv

load_dotenv("./dev/.env")

app = Flask(__name__)

app.register_blueprint(base)
app.register_blueprint(rc_register)
app.register_blueprint(rc_login)
app.register_blueprint(bp)
