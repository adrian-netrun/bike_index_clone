from flask import Blueprint


def write_to_file(err) -> None:
    file = open("error.txt", "a")
    file.write(str(err))
    file.write("\n")
    file.close()
    return None


bp = Blueprint("errors", __name__)


@bp.app_errorhandler(400)
def handle_DB_error(err):
    write_to_file(err)
    return "Username already in use, try again", 400
