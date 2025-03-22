from flask import Blueprint, session

rc_logout = Blueprint("logout", __name__, url_prefix="/api")


@rc_logout.route("/logout", methods=["POST"])
def logout():
    pass
