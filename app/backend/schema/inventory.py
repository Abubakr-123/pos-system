from pydantic import BaseModel , Field, ConfigDict


class Stoks(BaseModel):
    product_id:int
    stok_quantity:int
    movement_type:str

