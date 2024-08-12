from sqlalchemy import Integer, String, Boolean, Column
from sqlalchemy.orm import Mapped, mapped_column, foreign
from typing import Optional

from .database import Base



class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50))
    full_name: Mapped[Optional[str]] = mapped_column(String(150))
    hashed_password: Mapped[str] = mapped_column(String(1000))
    email: Mapped[str] = mapped_column(String(256))
    age: Mapped[Optional[int]]
    sex: Mapped[Optional[str]] = mapped_column(String(20))
    interests: Mapped[Optional[str]]
    language: Mapped[Optional[str]] = mapped_column(String(30))
    about: Mapped[Optional[str]] = mapped_column(String(10000))
    rating = Column('rating', Integer, default=0)
    disabled = Column('disabled', Boolean, default=False)


# class User(Base):
#     __tablename__ = "users"

#     id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
#     username: Mapped[str] = mapped_column(String(50))
#     full_name: Mapped[Optional[str]] = mapped_column(String(150))
#     hashed_password: Mapped[str] = mapped_column(String(1000))
#     email: Mapped[str] = mapped_column(String(256))
#     disabled: Mapped[bool]