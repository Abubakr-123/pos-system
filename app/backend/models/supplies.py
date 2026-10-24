from sqlalchemy.orm import Mapped , mapped_column , relationship
from sqlalchemy import Integer ,  ForeignKey , String
from app.backend.models.base import BaseModel
from app.backend.models.product import Product

class Supplies(BaseModel):
    __tablename__="supplers"
    name:Mapped[str]=mapped_column(String(100),nullable=False,index=True)
    phone:Mapped[int]=mapped_column(Integer(),nullable=False)
    product_id:Mapped[int]=mapped_column(Integer(),ForeignKey("products.id"))
    # product=Mapped["Product"]=relationship(back_populates="supplers")
