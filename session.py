import os
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

engine = "sqlite:///db_session.sqlite3"
session_db = SQLAlchemy()

sess = Session()
