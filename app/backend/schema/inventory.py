from pydantic import BaseModel , Field, ConfigDict


class StoksPay(BaseModel):
    product_id:int
    quantity:int=Field(gt=0)
    

