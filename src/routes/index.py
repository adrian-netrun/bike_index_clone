from flask import Blueprint, request, json, Response

base = Blueprint("index", __name__, url_prefix="/")


@base.route("/", methods=["GET"])
def index() -> None:
    if request.method == "GET":
        message = {"Message": "Server OK"}
        return Response(json.dumps(message), status=200, mimetype="application/json")
