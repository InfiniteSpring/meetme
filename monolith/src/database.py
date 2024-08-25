from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from .config import DB_PASS, DB_HOST, DB_NAME, DB_PORT, DB_USER
from sqlalchemy.orm import DeclarativeBase


DATABASE_URL = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(DATABASE_URL, echo=True)

class Base(DeclarativeBase):
    pass


async_session = async_sessionmaker(
    engine,
    expire_on_commit=False
)
