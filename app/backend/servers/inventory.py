from app.backend.models.inventory import Stock , StockMovement , MovementType
from app.backend.schema.inventory import StoksPay
from sqlalchemy.orm import Session 
from fastapi import HTTPException , status
from app.backend.schema.inventory import StoksPay

def change_stock(
    db:Session,
    product_id:int,
    quantity:int,
    movement_type:MovementType,
):
    if movement_type!=MovementType.ADJUSTMENT and quantity<=0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="quantity most be gearter than zero ")
    if movement_type==MovementType.ADJUSTMENT and quantity==0: 
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="quantity most be gearter than zero ") 
    
    increase_movement={
        MovementType.PAY,
        MovementType.CUSTOMER_RETURN
    }  
    
    decrase_movement={
        MovementType.DAMGE,
        MovementType.PAY_RETURN,
        MovementType.SALE
    }
    if movement_type in increase_movement:
        signed_quantity=quantity
    elif movement_type in decrase_movement:
        signed_quantity= -quantity
    else:
        signed_quantity=quantity
        
    inventory=db.query(Stock).filter(Stock.product_id==product_id).first()
    
    if not inventory:
        raise HTTPException(status_code=404,detail="not found")
    
    if inventory.quantity + signed_quantity <0:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="not enough Stock")
    inventory.quantity+=signed_quantity
    
    movement=StockMovement(
        product_id=product_id,
        quantit=signed_quantity,
        type=movement_type
        
    )
    db.add(movement)

def stock_pay(
    db:Session,
    data:StoksPay,
    product_id:int,
    movement_type:MovementType
):
    try:
        change_stock(
            db=db,
            product_id=product_id,
            quantity=data.quantity,
            movement_type=MovementType.PAY,
        )
        db.commit()
    except:
        db.rollback()
        raise