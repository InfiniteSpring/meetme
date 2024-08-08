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
    email: str | None = None
    full_name: str | None = None
    disabled: bool = False


class UserInDB(User):
    hashed_password: str


class DBUser(UserInDB):
    id: int


class UserCreate(User):
    password: str

