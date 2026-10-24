from re import S

from pydantic import BaseModel ,Field , ConfigDict

class CategoryCreate(BaseModel):
    name:str
    
class CategoryRespones(BaseModel):
    id:int
    name:str
    model_config=ConfigDict(from_attributes=True)