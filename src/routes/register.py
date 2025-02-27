from flask import Blueprint, make_response, request, Response, json
from werkzeug.security import generate_password_hash

rc_register = Blueprint("register", __name__, url_prefix="/api")

test_user_list = [
    {"username": "testuser@bikeindex.com"},
    {"username": "thisisalsoatest@bikeindex.com"},
]


def register_user(username, unhashed_password):
    try:
        hashed_password = generate_password_hash(
            unhashed_password, method="pbkdf2", salt_length=16
        )
        test_user_list.append({"username": username, "password": hashed_password})

        return True
    except Exception as e:
        raise Exception(f"Error with creating user: {e}")


def is_user_exist(username) -> bool:
    for itm in test_user_list:
        if itm["username"] == username:
            return True


@rc_register.route("/register", methods=["POST"])
def register() -> None:
    data = request.json

    user_exist = is_user_exist(data["username"])
    if user_exist is True:
        return Response(json.dumps({"User_exists": True}), status=409)

    try:
        register = register_user(data["username"], data["password"])
        if register is True:
            return Response(json.dumps({"User_created": True}), status=200)

    except Exception as e:
        raise Exception(f"Error with registering user: {e}")

    finally:
        for i in test_user_list:
            print(i)
