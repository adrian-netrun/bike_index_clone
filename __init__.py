from flask import Flask
from flask_bcrypt import Bcrypt

from .src.routes.index import base
from .src.routes.login import rc_login
from .src.routes.register import rc_register

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.register_blueprint(base)
app.register_blueprint(rc_register)
app.register_blueprint(rc_login)
