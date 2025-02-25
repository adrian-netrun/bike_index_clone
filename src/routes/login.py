from flask import Blueprint, request, Response, json
from werkzeug.security import generate_password_hash, check_password_hash

rc_login = Blueprint("login", __name__, url_prefix="/api")


def decrypt_password(hash, pt_password) -> bool:
    return check_password_hash(hash, pt_password)


@rc_login.route("/login", methods=["POST"])
def login() -> None:
    pw_hash = generate_password_hash("hellotester", method="pbkdf2", salt_length=10)
    print(pw_hash)
    if request.method == "POST":
        body = request.json
        is_password_true = decrypt_password(pw_hash, body["username"])

        if not is_password_true:
            return Response(status=401)
        else:
            return Response(json.dumps({"message": "create cookie here"}), status=200)
    else:
        return Response(
            json.dumps({"Message:": "Sever issue or url does not exist"}), status=403
        )
