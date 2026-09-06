from pydantic import BaseModel , Field

class ProductRespones(BaseModel):
    id:int
    name:str
    price:float

class ProductCreate(BaseModel):
    name:str
    price:float