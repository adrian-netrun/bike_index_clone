from flask import Blueprint, session, request, Response
from sqlalchemy import select
from werkzeug.security import check_password_hash
from ...db import db_session
from ..models.models import User

rc_login = Blueprint("login", __name__, url_prefix="/api")

type Exception = Exception


def fetch_user(request: dict[str]) -> tuple | Exception:
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
def login():
    data: dict = request.json
    row = fetch_user(data)
    try:
        check = check_password_hash(row[2], data["password"])
        if not check:
            raise Exception
        else:
            return Response(status=200).set_cookie("userid", row[0], "username", row[1])
        # this is not the correct way of handling things
    except Exception as error:
        print(error)
        return "password is wrong", 401
