
from sqlalchemy.orm import Mapped , mapped_column , relationship
from sqlalchemy import Integer ,  ForeignKey
from app.backend.models.base import BaseModel
from app.backend.models.product import Product

class stok(BaseModel):
    __tablename__="stokes"
    quantity:Mapped[int]=mapped_column(Integer())
    product_id:Mapped[int]=mapped_column(Integer(),ForeignKey("products.id"))
    # product:Mapped["Product"]=relationship(back_populates="stok")