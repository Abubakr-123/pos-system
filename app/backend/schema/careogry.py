from abc import update_abstractmethods
import datetime
from re import I
from unittest.mock import Base
from pydantic import BaseModel , ConfigDict , Field

class CategoryCreate(BaseModel):
    name:str=Field(min_length=1,max_length=20)


class CategoryRespones(BaseModel):
    id:int
    name:str
    create_at:datetime
    update_at:datetime
    model_config=ConfigDict(from_attributes=True)
