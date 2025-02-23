from flask import Blueprint, request, Response


ir_index = Blueprint("index", __name__)


@ir_index.route("/")
def index():
    if request.method == "GET":
        return Response.status_code(200)
