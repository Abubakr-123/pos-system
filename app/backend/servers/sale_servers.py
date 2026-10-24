from sys import exception
from app.backend.models.product import Product
from app.backend.models.sale import Sale , SaleItem
from app.backend.schema.sales import SaleCreate , SaleItemCreate ,SaleItemRespones ,SalesRespones
from sqlalchemy.orm import Session
from fastapi import HTTPException , status
from typing import Optional

def get_sale(db:Session,data:SalesRespones):
    sale=db.query(Sale).all()
    return sale

def create_sale(db:Session,data:SaleCreate):
    sub_total=0
    for item in data.items:
        if item.quntity<=0:
            raise HTTPException(status_code=400,detail="")
        product=db.query(Product).filter(Product.id==item.product_id).first()
        if not product:
            raise HTTPException(status_code=404,detail="not found")
    item_total=product.price*item.quntity
    sub_total+=item_total
    total=sub_total
    
    if data.discuont:
        total=sub_total-data.discuont
        
    try:    
        sale=Sale(
            discuont=data.discuont,
            subtotal=sub_total,
            total=total
        )
        db.add(sale)
    
        db.flush()
        for item in data.items:
            product=db.query(Product).filter(Product.id==item.product_id).first()
            if not product:
                raise HTTPException(status_code=404,detail="not found")
        sale_item=SaleItem(
            quntity=item.quntity,
            unit_price=product.price,
            sale_id=sale.id,
            product_id=product.id
        )
        db.add(sale_item)
        db.commit()
        db.refresh(sale)
        return sale
    except:
        db.rollback()
        raise
    
        

    
def update_sale(sale_id:int,data:SalesRespones,db:Session):
    sale=db.query(Sale).filter(Sale.id==sale_id).first()
    if not sale:
        raise HTTPException(status_code=404,detail="not found")
    update_data=data.model_dump(exclude_unset=True)
    for key , value  in  update_data.items:
        setattr(sale , key , value)
    db.commit()
    db.refresh(sale)
    return sale

def delete_sale(sale_id:int, db:Session):
    sale=db.query(Sale).filter(Sale.id==sale_id).first()
    if not sale:
        raise HTTPException(status_code=404,detail="not found")
    db.delete(sale)
    db.commit()

        