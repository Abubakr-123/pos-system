from sqlalchemy import Integer , String , Float
from sqlalchemy.orm import Mapped , mapped_column , relationship
from app.backend.models.base import BaaeModel
from typing import TYPE_CHECKING
from enum import Enum
from sqlalchemy import Enum as SQLENUM

class UserRole(str , Enum):
    CASHER="CASHER"
    MANAGER="MANAGER"


class User(BaaeModel):
    __tablename__="users"
    name:Mapped[str]=mapped_column(String(50),nullable=False,index=True)
    email:Mapped[str]=mapped_column(String(50),nullable=False,unique=True)
    hash_password:Mapped[str]=mapped_column(String(50),nullable=False)
    role:Mapped[UserRole]=mapped_column(SQLENUM(),default=UserRole.CASHER)