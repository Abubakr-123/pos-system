from sqlalchemy import create_engine 
from sqlalchemy.orm import DeclarativeBase , sessionmaker
import os

ROOT_PATH=os.path.dirname(os.path.realpath(__file__))
DB_URI=os.path.join(ROOT_PATH,"pos.db")
engine=create_engine(f"sqlite:///{DB_URI}",echo=True)
sessionlocal=sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

def get_db():
    db=sessionlocal()
    try:
        yield db
    finally:
        db.close()