from sqlalchemy.orm import Session 
from app.backend.models.caregory import Category
from app.backend.schema.careogry import CategoryCreate , CategoryRespones
from typing import Optional 
from fastapi import HTTPException , status


def get_category(data:CategoryRespones, db:Session):
    category=db.query(Category).all()
    return category

def create_category(db:Session, data:CategoryCreate):
    category=Category(**data.model_dump())
    db.add(category)
    db.commit()
    db.refresh(category)
    return category

def update_category(cate_id:int,db:Session,data:CategoryRespones):
    category=db.query(Category).filter(Category.id==cate_id).first()
    if not category :
        raise HTTPException(status_code=404 , detail="not found")
    update_data=data.model_dump(exclude_unset=True)
    for key , value in update_data.items:
        setattr(category , key , value)
    db.commit()
    db.refresh(category)
    return category

def delete_category(cate_id:int, db:Session):
    category=db.query(Category).filter(Category.id==cate_id).first()
    if not category :
        raise HTTPException(status_code=404 , detail="not found")
    db.delete(category)
    db.commit()
