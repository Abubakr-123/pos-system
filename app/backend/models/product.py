from sqlalchemy import Integer , String , Float , ForeignKey
from sqlalchemy.orm import Mapped , mapped_column , relationship
from app.backend.models.base import BaseModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.backend.models.caregory import Category
    from app.backend.models.sale import SaleItem
    from app.backend.models.inventory import StockMovement , Stock


class Product(BaseModel):
    __tablename__="products"
    name:Mapped[str]=mapped_column(String(50),nullable=False,index=True)
    price:Mapped[float]=mapped_column(Float(),nullable=False)
    category_id:Mapped[int]=mapped_column(Integer(),ForeignKey("caregorys.id"))
    cateogry:Mapped["Category"]=relationship(back_populates="product")
    saleitem:Mapped["SaleItem"]=relationship(back_populates="product")
    stockmovement:Mapped["StockMovement"]=relationship(back_populates="product")
    stock:Mapped["Stock"]=relationship(back_populates="product")