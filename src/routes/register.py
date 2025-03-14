import os
from flask import Blueprint, request, Response, json
from werkzeug.security import generate_password_hash
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from ..error_handler import handle_DB_error
from ..db.models import User

db_engine = create_engine(
    os.environ["DB_URI"],
    echo=True,
)

rc_register = Blueprint("register", __name__, url_prefix="/api")


def register_user(username, unhashed_password) -> None:
    hashed_password = generate_password_hash(
        unhashed_password, method="pbkdf2", salt_length=16
    )
    with Session(db_engine) as session:
        try:
            user = User(username=username, hashed_password=hashed_password)
            session.add(user)
            session.commit()
            return True
        except IntegrityError as err:
            handle_DB_error(err)
            return err
        finally:
            session.close()
            return False


def is_user_exist(username) -> bool:
    pass


@rc_register.route("/register", methods=["POST"])
def register():
    data = request.json

    user_exist = is_user_exist(data["username"])
    if user_exist is True:
        return Response(json.dumps({"User_exists": True}), status=409)

    try:
        register = register_user(data["username"], data["password"])
        if register is True:
            return Response(json.dumps({"User_created": True}), status=200)
        else:
            raise Exception("Duplicate user or other Database type error")

    except Exception as err:
        return handle_DB_error(err)
