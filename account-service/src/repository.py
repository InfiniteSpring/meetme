from sqlalchemy import select

from .schemas import UserInDB, DBUser
from .models import User
from .database import async_session


class UserRepository:

    @classmethod
    async def get_user_by_username(
        cls, 
        username: str
    ):
        async with async_session() as session:
            query = select(User).filter(User.username == username).limit(1)
            result = await session.execute(query)
            result_model = result.scalars().first()
            return result_model


    @classmethod
    async def get_all_users(
        cls
    ):
        async with async_session() as session:
            query = select(User)
            result = await session.execute(query)
            user_models = result.scalars().all()
            return user_models


    
    @classmethod
    async def create_user(
        cls,
        user: UserInDB
    ):
        async with async_session() as session:
            try:
                user_dict = user.model_dump()
                user = User(**user_dict)  
                session.add(user)
                await session.flush()
                await session.commit()
                return user
            except Exception as e:
                return e


    
    @classmethod
    async def change_user(user: UserInDB):
        ...

    
    @classmethod
    async def delete_user(user_id: int):
        ...
