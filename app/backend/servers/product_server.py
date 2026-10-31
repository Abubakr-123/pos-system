from app.backend.database.database import get_db
from app.backend.schema.product_s import ProductCreate ,ProductRespones
from app.backend.models.product import Product
from sqlalchemy.orm import Session
from fastapi import HTTPException , status
from typing import Optional
from app.backend.models.inventory import Stock


def get_porduct(db:Session ,
                 data:ProductRespones,
                 sarech:Optional[str]=None,
                 page:int=1,
                 page_size:int=20
                 ):
    product=db.query(Product).all()
    ofset=(page-1)*page_size
    
    return product


def create_product(db:Session, data:ProductCreate):
    try:
        product=Product(**data.model_dump())
        db.add(product)
        db.flush()
        inventory=Stock(
            product_id=product.id,
            quantity=0
        )
        db.add(inventory)
        db.commit()
        db.refresh(product)
        return product
    except:
        db.rollback()
        raise
       

def update_product(product_id:int,db:Session,data:ProductRespones):
    product=db.query(Product).filter(Product.id==product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")
    
    update_data=data.model_dump(exclude_unset=True)
    for key , value in update_data.items:
        setattr(product , key , value)
    db.commit()
    db.refresh(product)
    return product

def delete_product(product_id:int , db:Session ):
    product=db.query(Product).filter(Product.id==product_id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")
    db.delete(product)
    db.commit()
    
