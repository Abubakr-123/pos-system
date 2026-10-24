from pydantic import BaseModel , Field , ConfigDict



class SupplersCreate(BaseModel):
    name:str
    email:str
    phone:int
    product_sup:str

class SupplersRespones(SupplersCreate):
    id:int

