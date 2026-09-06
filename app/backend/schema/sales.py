from pydantic import BaseModel , ConfigDict

class SaleItemCreate(BaseModel):
    product_id:int
    quntity:int

class SaleCreate(BaseModel):
    discuont:int=0
    items:list[SaleItemCreate]

class SaleItemRespones(BaseModel):
    id:int
    product_id:int
    quntity:int
    unit_price:float

class SalesRespones(BaseModel):
    id:int
    subtotal:float
    dicuont:int
    total:float
    items:list[SaleItemRespones]
    model_config=ConfigDict(from_attributes=True)

