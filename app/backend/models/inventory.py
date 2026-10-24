
from sqlalchemy.orm import Mapped , mapped_column , relationship
from sqlalchemy import Integer ,  ForeignKey , String
from app.backend.models.base import BaseModel
from app.backend.models.product import Product
from enum import Enum
from sqlalchemy import Enum as SQLEnum

class MovementType(str, Enum):
    PAY="PAY"
    SALE="SALE"
    CUSTOMER_RETURN="CUSTOMER_RETURN"
    PAY_RETURN="PAY_RETURN"
    DAMGE="DANGE"

class Stock(BaseModel):
    __tablename__="stokes"
    quantity:Mapped[int]=mapped_column(Integer())
    product_id:Mapped[int]=mapped_column(Integer(),ForeignKey("products.id"))
    product:Mapped["Product"]=relationship(back_populates="stock")

class StockMovement(BaseModel):
    __tablename__="stockmovements"
    type:Mapped[SQLEnum]=mapped_column(String(20),default=MovementType.SALE)
    product_id:Mapped[int]=mapped_column(Integer(), ForeignKey("products.id"))
    quantit:Mapped[int]=mapped_column(Integer())
    product:Mapped["Product"]=relationship(back_populates="stockmovement")

