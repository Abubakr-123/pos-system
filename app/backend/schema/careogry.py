
from pydantic import BaseModel , ConfigDict , Field

class CategoryCreate(BaseModel):
    name:str=Field(min_length=1,max_length=20)


class CategoryRespones(BaseModel):
    id:int
    name:str
    create_at:int
    update_at:int
    model_config=ConfigDict(from_attributes=True)
