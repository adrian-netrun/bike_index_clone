from flask import Blueprint, request, Response


home_route = Blueprint("landingpage", __name__)


@home_route.route("/")
def landing_page():
    if request.method == "GET":
        return Response.status_code(200)
