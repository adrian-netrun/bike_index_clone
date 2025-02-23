from flask import Flask
from .routes.auth import auth_router
from .routes.home import ir_index

app = Flask(__name__)

app.register_blueprint(ir_index, url_prefix="/indexb")
app.register_blueprint(auth_router, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
