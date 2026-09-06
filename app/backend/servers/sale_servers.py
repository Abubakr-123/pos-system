from sys import exception
from app.backend.models.product import Product
from app.backend.models.sale import Sale , SaleItem
from app.backend.schema.sales import SaleCreate , SaleItemCreate ,SaleItemRespones ,SalesRespones
from sqlalchemy.orm import Session
from fastapi import HTTPException , status
from typing import Optional


def get_sales(db:Session,data:SalesRespones):
    sale=db.query(Sale).all()
    return sale

def create_sale(db:Session,data:SaleCreate):
    subtotal=0
    for item in data.items:
        if item.quntity<=0:
            raise HTTPException(status_code=404,detail="not found")
        product=db.query(Product).filter(Product==item.product_id).first()
        if not product:
            raise HTTPException(status_code=404,detail="not found")
    
    item_total=product.price*item.quntity
    subtotal+=item_total

    if data.discuont:
        total=subtotal-data.discuont
    try:
        sale=Sale(
            discuont=data.discuont,
            subtotal=subtotal,
            total=total
        )
        db.add(sale)
        db.flush()

        for item in data.items:
            product=db.query(Product).filter(Product==item.product_id).first()

        saleitem=SaleItem(
            quntity=item.quntity,
            product_id=product.id,
            sale_id=sale.id
        )

        db.add(saleitem)
        db.commit()
    except exception:
        db.rollback() 
        raise
        