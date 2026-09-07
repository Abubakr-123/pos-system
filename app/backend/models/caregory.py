from sqlalchemy import Integer , String , Float
from sqlalchemy.orm import Mapped , mapped_column ,relationship
from app.backend.models.base import BaseModel
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.backend.models.product import Product

class Category(BaseModel):
    __tablename__="categorys"
    name:Mapped[str]=mapped_column(String(20),nullable=False)
    product:Mapped["Product"]=relationship(back_populates="category")

