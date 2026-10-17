from hmac import new
from app.backend.models.product import Product
from app.backend.scheam.product import ProductCreate , ProductRespones
from sqlalchemy.orm import Session
from fastapi import HTTPException , status


def get_product(
        db:Session,
        data:ProductRespones,
        page:int=0,
        page_size:int=20,
):
    product=db.query(Product).all()
    return product

def create_product(db:Session,data:ProductCreate):
    new_product=Product(**data.model_dump())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

def update_product(db:Session,data:ProductRespones,product_id:int):
    product=db.query(Product).filter(Product.id==product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="not found")
    updata_data=data.model_dump(exclude_unset=True)
    for key , value in updata_data.items:
        setattr(product,key,value)

    db.commit()
    db.refresh(product)
    return product
def delete_product(product_id:int,db:Session):
    product=db.query(Product).filter(Product.id==product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="not found")
    db.delete(product)
    db.commit()