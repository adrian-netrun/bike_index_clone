from sqlalchemy import create_engine, text, MetaData, Table
from dotenv import load_dotenv
import os

load_dotenv()

username = os.environ.get("DB_USERNAME")
password = os.environ.get("DB_PASSWORD")
hostname = os.environ.get("DB_HOSTNAME")
db_name = os.environ.get("Db_DBNAME")

connection_string = (
    "mariadb+pymysql://adrian-dev:hellodatabase@localhost/bikeindex?charset=utf8mb4"
)

engine = create_engine(connection_string, echo=True)

metadata_obj = MetaData()

user_table = Table("User", metadata_obj, autoload_with=engine)
print(user_table)
