from sqlalchemy import Integer , String , Float , ForeignKey
from sqlalchemy.orm import Mapped , mapped_column ,relationship
from app.backend.models.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.backend.models.product import Product

class Sale(BaseModel):
    __tablename__="sales"
    discuont:Mapped[int]=mapped_column(Integer())
    subtotal:Mapped[float]=mapped_column(Float())
    total:Mapped[float]=mapped_column(Float)
    saleitem:Mapped["SaleItem"]=relationship(back_populates="sale")


class SaleItem(BaseModel):
    __tablename__="saleitems"
    quntity:Mapped[int]=mapped_column(Integer(),nullable=False)
    unit_price:Mapped[float]=mapped_column(Float)
    sale:Mapped["Sale"]=relationship(back_populates="saleitem")
    sale_id:Mapped[int]=mapped_column(Integer(),ForeignKey("sales.id"))
    product_id:Mapped[int]=mapped_column(ForeignKey("products.id"))
    product:Mapped["Product"]=relationship(back_populates="saleitem")
