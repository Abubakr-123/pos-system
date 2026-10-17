from pydantic import BaseModel , ConfigDict ,Field

class ProductCreate(BaseModel):
    name:str
    price:float
    categoey_id:int


class ProductRespones(ProductCreate):
    id:int