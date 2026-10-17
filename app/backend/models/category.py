from sqlalchemy import Integer , String , Float
from sqlalchemy.orm import Mapped , mapped_column , relationship
from app.backend.models.base import BaaeModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.backend.models.product import Product

class Category(BaaeModel):
    __tablename__="categores"
    name:Mapped[str]=mapped_column(String(50),nullable=False,index=True)
    product:Mapped["Product"]=relationship(back_populates="category")
