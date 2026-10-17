from sqlalchemy import Integer , String , Float , ForeignKey
from sqlalchemy.orm import Mapped , mapped_column , relationship
from app.backend.models.base import BaaeModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.backend.models.category import Category


class Product(BaaeModel):
    __tablename__="products"
    name:Mapped[str]=mapped_column(String(50),nullable=False,index=True)
    price:Mapped[float]=mapped_column(Float(),nullable=False)
    category_id:Mapped[int]=mapped_column(Integer(),ForeignKey("categores.id"))
    cateogry:Mapped["Category"]=relationship(back_populates="product")