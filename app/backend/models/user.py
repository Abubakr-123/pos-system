from sqlalchemy.orm import Mapped ,  mapped_column , relationship
from sqlalchemy import Integer , String
from app.backend.models.base import BaseModel
from enum import Enum
from sqlalchemy import Enum as SqlEnum

class UserRole(str,Enum):
    CASHER="casher"
    MANAGER="manager"


class User(BaseModel):
    __tablename__="users"
    username:Mapped[str]=mapped_column(String(50),nullable=False,unique=True)
    hash_password:Mapped[str]=mapped_column(String(50),nullable=False)
    role:Mapped[UserRole]=mapped_column(SqlEnum(UserRole),default=UserRole.CASHER)
    def __repr__(self):
        return f"<User{self.username}>"
