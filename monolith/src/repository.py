from sqlalchemy import select, update
from sqlalchemy.orm import defer

from .schemas import UserInDB
from .models import User
from .database import async_session


class UserRepository:


    @classmethod
    async def get_user_by_username(
        cls, 
        username: str
    ):
        async with async_session() as session:
            query = select(User).filter(User.username==username).limit(1)
            result = await session.execute(query)
            result_model = result.scalars().first()
            return result_model


    @classmethod
    async def get_created_date_by_id(
        cls, user_id: int
    ):
        async with async_session() as session:
            query = select(User.created_at).where(User.id==user_id)
            result = await session.execute(query)
            return result.scalars().first()


    @classmethod
    async def get_all_users(
        cls
    ):
        async with async_session() as session:
            query = select(User).options(defer(User.hashed_password))
            # query = select(User)
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
    async def change_user(
        cls,
        user: UserInDB
    ):
        async with async_session() as session:
            stmt = update(User).where(User.username == user.username)\
                .values(
                    username=user.username, 
                    email=user.email,
                    full_name=user.full_name,
                    hashed_password=user.hashed_password,
                    age=user.age,
                    sex=user.sex,
                    interests=user.interests,
                    language=user.language,
                    about=user.about
                    )
            await session.execute(stmt)
            await session.commit()
            return await cls.get_user_by_username(username=user.username)


    @classmethod
    async def delete_user(user_id: int):
        ...

