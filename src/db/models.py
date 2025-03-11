from dotenv import load_dotenv
from typing import List
from typing import Optional
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy import String, DateTime, Integer, Boolean
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
    updated_at = mapped_column(DateTime(timezone=True), onupdate=func.utcnow())

    def __repr__(self):
        pass


class User(Base):
    __tablename__ = "User"

    username = mapped_column(String(300), nullable=False, unique=True)
    hashed_password = mapped_column(String(10000), nullable=False)
    user_profile: Mapped["UserProfile"] = relationship(uselist=False)
    has_admin: Mapped["HasAdmin"] = relationship(uselist=False)


class UserProfile(Base):
    __tablename__ = "UserProfile"
    # __table_args__ = (UniqueConstraint("user_id"),)

    displayname = mapped_column(String(100), nullable=False)
    bio = mapped_column(String(500), nullable=False)
    # this is a many to one relationship - I will need to check how this should be implemented
    # this calls cannot be instatiated with this here, must be some kind of Dep Injection or something
    displayname = mapped_column(String(500))
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), unique=True)
    # Many to one relation for Posts
    posts: Mapped[List["Post"]] = relationship(uselist=True)
    comment: Mapped[List["Comment"]] = relationship(uselist=True)


class HasAdmin(Base):
    __tablename__ = "HasAdmin"
    # only one or zero allowed
    is_admin: Mapped[int] = mapped_column(Boolean, nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("User.id"), unique=True)


class Post(Base):
    __tablename__ = "Post"

    make: Mapped[str] = mapped_column(String(200), nullable=False)
    model: Mapped[str] = mapped_column(String(200), nullable=False)
    serial: Mapped[str] = mapped_column(String(60), nullable=False)
    description: Mapped[str] = mapped_column(String(600))
    # UserProfile - Post relationship
    user_profile_id: Mapped[int] = mapped_column(ForeignKey("UserProfile.id"))
    # Imaage - Post relationship
    images: Mapped[List["Image"]] = relationship(uselist=True)
    comment: Mapped[List["Comment"]] = relationship(uselist=True)


class Image(Base):
    __tablename__ = "Image"

    path: Mapped[str] = mapped_column(String(300), nullable=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("Post.id"), unique=True)


class Comment(Base):
    __tablename__ = "Comment"

    user_profile_id: Mapped[int] = mapped_column(ForeignKey("UserProfile.id"))
    comment_content: Mapped[int] = mapped_column(String(500), nullable=False)
    post_id: Mapped[int] = mapped_column(ForeignKey("Post.id"))
