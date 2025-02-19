from flask import Flask
from .routes.auth import auth_router
from .routes.home import home_route

app = Flask(__name__)

app.register_blueprint(home_route, url_prefix="/")
app.register_blueprint(auth_router, url_prefix="/api")

if __name__ == "__main__":
    app.run(debug=True)
