"""router"""
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from typing import Annotated
from datetime import timedelta, datetime, timezone
from passlib.context import CryptContext
from jwt.exceptions import InvalidTokenError
import jwt

from .config import ACCESS_TOKEN_EXPIRE_MINUTES, SECRET_KEY, ALGORITHM
from .schemas import *
from .service import *

from .config import logger


main_router = APIRouter(
    prefix="/users",
    tags=["Account"]
)


@main_router.post("/token")
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
) -> Token:
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return Token(access_token=access_token, token_type="bearer")


@main_router.get("/me", response_model=UserView)
async def read_users_me(
    current_user: Annotated[UserView, Depends(get_current_active_user)],
):
    return current_user


@main_router.get("/me/items")
async def read_own_items(
    current_user: Annotated[User, Depends(get_current_active_user)],
):
    return [{"item_id": "Foo", "owner": current_user.username}]


# ----------------------------------------------------------


@main_router.post("/create")
async def create_user(
    user: Annotated[UserCreate, Depends()]
):
    response = await create_user_service(user)
    return response


@main_router.get("/all")
async def get_all_users():
    result = await get_all_users_service()
    return result


@main_router.get("/user/{username}")
async def get_user_by_username(username:str):
    result = await get_user_by_username_service(username)
    return result


@main_router.put('/update')
async def update_one(
    current_user: Annotated[UserCreate, Depends(get_current_active_user)],
    # user: Annotated[UserCreate, Depends()]
):
    try:
        result = await update_user_service(user=current_user)
        return result
    except Exception as e:
        logger.error(f"{'-'*16}There was an error -> {e}")
        return {
            "success": False,
            "details": {
                "error": e
            }
        }

@main_router.get('/get_creation_date/{id}')
async def get_creation_date(id: int):
    return await get_user_created_date_by_id_service(id)