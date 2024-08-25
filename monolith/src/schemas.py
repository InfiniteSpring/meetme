from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class LoginShema(BaseModel):
    username: str
    password: str


class TokenData(BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str
    full_name: str | None = None
    age: int | None = None
    sex: str | None = None
    interests: str | None = None
    language: str | None = None
    about: str | None = None


class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    full_name: str | None = None
    age: int | None = None
    sex: str | None = None
    interests: str | None = None
    language: str | None = None
    about: str | None = None


class UserView(User):
    disabled: bool
    rating: int
    # created_at: DateTime



class UserInDB(User):
    hashed_password: str


class DBUser(UserInDB):
    id: int

