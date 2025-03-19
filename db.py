from sqlalchemy import DateTime
from sqlalchemy import create_engine
from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    DeclarativeBase,
    mapped_column,
    Mapped,
)
from sqlalchemy.sql import func


engine = create_engine(
    "mariadb+pymysql://adrian-dev:hellodatabase@localhost/bikeindex2?charset=utf8mb4"
)
db_session = scoped_session(
    sessionmaker(autoflush=False, autocommit=False, bind=engine)
)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False
    )

    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), onupdate=func.utcnow())

    def __repr__(self):
        pass
