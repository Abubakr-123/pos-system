from sqlalchemy.orm import Mapped ,mapped_column
from datetime import datetime , UTC
from app.backend.database.database import Base
from sqlalchemy import Integer , DateTime, lambda_stmt

class BaseModel(Base):
    __abstract__=True
    id:Mapped[int]=mapped_column(Integer(),primary_key=True)
    create_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda:datetime.now(UTC))
    updtae_at:Mapped[datetime]=mapped_column(DateTime(timezone=True),default=lambda:datetime.now(UTC),onupdate=True)
    