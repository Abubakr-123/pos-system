from pydantic import BaseModel , Field , ConfigDict

class UsersCreate(BaseModel):
    username:str
    hash_password:str=Field(min_length=8,max_length=20)


class UserRespones(BaseModel):
    id:int
    username:str
    role:str


