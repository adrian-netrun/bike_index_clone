import os
from flask import Blueprint, request, json, make_response
from werkzeug.security import generate_password_hash
from sqlalchemy.exc import IntegrityError
from ..models.models import User
from ...db import db_session

rc_register = Blueprint("register", __name__, url_prefix="/api")


@rc_register.route("/register", methods=["POST"])
def register():
    data = request.json
    print(data["password"])
    hashed_password = generate_password_hash(
        data["password"], method="pbkdf2", salt_length=16
    )

    new_user = User(username=data["username"], hashed_password=hashed_password)

    try:
        with db_session() as session:
            session.add(new_user)
            session.commit()
    except Exception as error:
        print(error)
        return "User already exists", 400

    return "Completed correctly", 200
