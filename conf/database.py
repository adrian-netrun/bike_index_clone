from sqlalchemy import create_engine, text

engine = create_engine(
    "mariadb+pymysql://adrian-dev:hellodatabase@localhost/bikeindex?charset=utf8"
)

with engine.connect() as connection:
    result = connection.execute(text("Select * from User"))
    for r in result:
        print(r.id, r.username, r.passwordhash)
