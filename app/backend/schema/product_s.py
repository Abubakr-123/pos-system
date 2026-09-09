from pydantic import BaseModel , Field

class ProductRespones(BaseModel):
    id:int
    name:str
    price:float

class ProductCreate(BaseModel):
    category_id : int
    name:str
    price:float