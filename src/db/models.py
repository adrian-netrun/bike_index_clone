from dotenv import load_dotenv
from typing import List
from typing import Optional
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import UniqueConstraint

load_dotenv("../../.env")


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(
        primary_key=True, autoincrement=True, nullable=False
    )

    created_at = mapped_column(DateTime(timezone=True), server_default=func.now())
    updated_at = mapped_column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        pass


class User(Base):
    __tablename__ = "User"

    username = mapped_column(String(300), nullable=False)
    hashed_password = mapped_column(String(10000), nullable=False)
    user_profile: Mapped["UserProfile"] = relationship(
        back_populates="UserProfile", uselist=False
    )


class UserProfile(Base):
    __tablename__ = "UserProfile"
    # __table_args__ = (UniqueConstraint("user_id"),)

    displayname = mapped_column(String(100), nullable=False)
    bio = mapped_column(String(500), nullable=False)
    # this is a many to one relationship - I will need to check how this should be implemented
    # this calls cannot be instatiated with this here, must be some kind of Dep Injection or something
    displayname = mapped_column(String(500))
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), unique=True)
    user: Mapped["User"] = relationship(back_populates="User")


# class AdminRoles(Base):
#     pass


class Post(Base):
    __tablename__ = "Posts"

    make: Mapped[str] = mapped_column(String(200), nullable=False)
    model: Mapped[str] = mapped_column(String(200), nullable=False)
    serial: Mapped[str] = mapped_column(String(60), nullable=False)
    description: Mapped[str] = mapped_column(String(600))


class Images(Base):
    __tablename__ = "Images"

    path: Mapped[str] = mapped_column(String(300), nullable=True)


# class Comment(Base):
#     pass
