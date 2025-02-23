from flask import Blueprint, request, make_response
from ..mods.data_access import RunDatabaseQuery

auth_router = Blueprint("authorisation", __name__)


@auth_router.route("/api/register", methods=["POST"])
def register():
    pass


@auth_router.route("/login", methods=["POST"])
def login():
    if request.method == "POST":
        data = request.get_json()
        args = data["username"]
        query = format("Call SelectOneUser(?), [{args}]", args)
        query = RunDatabaseQuery(query).run_read_query()
        print(query)
        print(query.all())

    else:
        response = make_response("Not OK", 405)
        return response

    response = make_response("OK", 201)
    return response
