from flask import Blueprint, request, make_response

auth_router = Blueprint("authorisation", __name__)


@auth_router.route("/api/register", methods=["POST"])
@auth_router.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        print(data)
    else:
        response = make_response("Not OK", 405)
        return response

    response = make_response("OK", 201)
    return response
