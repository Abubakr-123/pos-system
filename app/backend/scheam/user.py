from pydantic import BaseModel ,Field ,ConfigDict

class UserBase(BaseModel):
    username:str
    email:str

class Users(UserBase):
    password_hash:str

class TokenDate(BaseModel):
    username:str | None=None

class Token(BaseModel):
    access_token:str
    token_type:str
