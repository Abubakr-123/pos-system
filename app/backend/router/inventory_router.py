from app.backend.models.inventory import Stock , MovementType
from sqlalchemy.orm import Session
from app.backend.servers  import inventory
from app.backend.database.database import get_db
from fastapi import Depends , APIRouter
from app.backend.schema.inventory import StoksPay

router=APIRouter(prefix="/Stock", tags=["stocks"])

@router.post("/")
def stock_pay(
    product_id:int,
    movement_type:MovementType,
    data:StoksPay,
    db:Session=Depends(get_db),
):
    try:
        inventory.stock_pay(db=db , data=data , product_id=product_id, movement_type=movement_type)
        return {"massage":"add seccs"}
    except:
        raise