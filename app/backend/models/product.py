from sqlalchemy import Integer , String , Float , ForeignKey
from sqlalchemy.orm import Mapped , mapped_column ,relationship
from app.backend.models.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.backend.models.caregory import Category
    from app.backend.models.sale import SaleItem


class Product(BaseModel):
    __tablename__="products"
    id:Mapped[int]=mapped_column(Integer(),primary_key=True)
    name:Mapped[str]=mapped_column(String(20),nullable=False)
    price:Mapped[float]=mapped_column(Float(),nullable=False)
    category_id:Mapped[int]=mapped_column(Integer(),ForeignKey("categorys.id"))
    category:Mapped["Category"]=relationship(back_populates="product")
    saleitem:Mapped["SaleItem"]=relationship(back_populates="product")