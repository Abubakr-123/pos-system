from turtle import update
from sqlalchemy import Integer , DateTime
from sqlalchemy.orm import Mapped , mapped_column
from datetime import datetime , timezone , UTC
from app.backend.database.database import Base

class BaseModel(Base):
    __abstract__=True
    id:Mapped[int]=mapped_column(Integer(),primary_key=True, index=True)
    create_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda:datetime.now(UTC))
    update_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda:datetime.now(UTC))
    