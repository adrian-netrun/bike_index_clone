from flask import Blueprint, request, Response, json, make_response
from sqlalchemy import select
from werkzeug.security import check_password_hash
from ...db import db_session
from ..models.models import User

rc_login = Blueprint("login", __name__, url_prefix="/api")

type = Exception = Exception


def fetch_users_password(request: dict[str]) -> tuple | Exception:
    with db_session() as sesssion:
        try:
            find_user = select(User.id, User.username, User.hashed_password).where(
                User.username == request["username"]
            )
            row = sesssion.execute(find_user).one()
            return row
        except Exception as NoResultFound:
            print(NoResultFound)
            return


@rc_login.route("/login", methods=["POST"])
def login() -> None:
    data: dict = request.json
    row = fetch_users_password(data)
    try:
        check = check_password_hash(row[2], data["password"])
        if not check:
            raise Exception
        # this is not the correct way of handling things
    except Exception as error:
        print(error)
        return "password is wrong", 401

    return "login route hit", 200
