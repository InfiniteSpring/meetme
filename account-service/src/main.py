"""main module for account-service"""
from fastapi import Depends, FastAPI
from contextlib import asynccontextmanager

from .database import Base, engine
from .router import main_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    print("server start working")
    # async with engine.begin() as conn:
    #     await conn.run_sync(Base.metadata.drop_all)
    #     await conn.run_sync(Base.metadata.create_all)
    print("db is ready to use")
    yield
    print("server stop working")


app = FastAPI(lifespan=lifespan)
app.include_router(main_router)


@app.get("/")
async def get_homepage():
    return {
        "data": "welcome to homepage"
    }