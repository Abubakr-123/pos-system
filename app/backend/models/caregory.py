from sqlalchemy import Integer , String , Float
from sqlalchemy.orm import Mapped , mapped_column ,relationship
from app.backend.database.database import Base 
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.backend.models.product import Product

class Category(Base):
    __tablename__="categorys"
    id:Mapped[int]=mapped_column(Integer(),primary_key=True)
    name:Mapped[str]=mapped_column(String(20),nullable=False)
    product:Mapped["Product"]=relationship(back_populates="category")

