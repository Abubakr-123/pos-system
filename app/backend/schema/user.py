from pydantic import BaseModel , Field , ConfigDict



class UsersCreate(BaseModel):
    username:str
    hash_password:str=Field(min_length=8,max_length=20)


class UserRespones(BaseModel):
    id:int
    username:str
    role:str
    model_config=ConfigDict(from_attributes=True)

class UserLogin(BaseModel):
    username:str
    password:str


class Token(BaseModel):
    token_access:str
    token_type:str
    
class RefreshToken(BaseModel):
    refresh_tkoen:str