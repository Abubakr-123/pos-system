from re import S
from fastapi import HTTPException , status
from app.backend.models.supplies import Supplies
from app.backend.schema.supplers import SupplersCreate , SupplersRespones
from sqlalchemy.orm import Session


def get_sup(data:SupplersRespones,db:Session):
    sup=db.query(Supplies).all()
    if not sup:
        raise HTTPException(status_code=404,detail="not found")
    return sup

def create_sup(data:SupplersCreate,db:Session):
    sup=Supplies(**data.model_dump())
    db.add(sup)
    db.commit()
    db.refresh(sup)

def update_sup(data:SupplersRespones,db:Session,sup_id:int):
    sup=db.query(Supplies).filter(Supplies.id==sup_id).first()
    if not sup :
        raise HTTPException(status_code=404, detail="not found")
    update_data=data.model_dump(exclude_unset=True)
    for key , value in update_data.items:
        setattr(sup , key , value)
    db.commit()
    db.refresh(sup)
    return sup
