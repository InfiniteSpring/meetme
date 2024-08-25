from sqlalchemy import Integer, String, Boolean, Column, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import Optional, List
from datetime import datetime

from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username = Column('username', String(32), unique=True, nullable=False)
    full_name: Mapped[Optional[str]] = mapped_column(String(150))
    hashed_password: Mapped[str] = mapped_column(String(1000))
    email: Mapped[str] = mapped_column(String(256))
    age: Mapped[Optional[int]]
    sex: Mapped[Optional[str]] = mapped_column(String(20))
    interests: Mapped[Optional[str]]
    language: Mapped[Optional[str]] = mapped_column(String(30))
    about: Mapped[Optional[str]] = mapped_column(String(10000))
    rating = Column('rating', Integer, default=0)
    created_at = Column('created_at', DateTime, default=datetime.now)
    disabled = Column('disabled', Boolean, default=False)
    posts: Mapped[Optional[List["Post"]]] = relationship(back_populates="user", cascade="all, delete")


class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    text: Mapped[str] = String(4096)
    rating = Column("rating", Integer, default=0)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE", onupdate="CASCADE"))
    user: Mapped["User"] = relationship(back_populates="user_posts", cascade="all, delete")


# class UserComment(Base):
#     __tablename__ = "account_comments"

#     id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
#     text: Mapped[str] = String(2048)
#     rating = Column("rating", Integer, default=0)
#     sender_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     recipient_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))


# class PostComment(Base):
#     __tablename__ = "posts_comments"

#     id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
#     text: Mapped[str] = String(2048)
#     rating = Column("rating", Integer, default=0)
#     sender_user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
#     recipient_post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))
