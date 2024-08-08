from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column, foreign

from .database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    username: Mapped[str] = mapped_column(String(50))
    full_name: Mapped[str] = mapped_column(String(150))
    hashed_password: Mapped[str] = mapped_column(String(1000))
    email: Mapped[str] = mapped_column(String(256))
    disabled: Mapped[bool]

