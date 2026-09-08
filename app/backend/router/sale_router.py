from ast import Return
from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
from app.backend.database.database import get_db
from app.backend.models import sale
from app.backend.models.sale import Sale , SaleItem
from app.backend.schema.sales import SaleCreate ,SaleItemCreate , SaleItemRespones ,SalesRespones
from app.backend.servers import sale_servers


router=APIRouter(prefix="/Sale", tags=["sales"])

@router.get("/",response_model=SaleItemRespones)
def get_sales(data:SalesRespones,db:Session=Depends(get_db)):
    return sale_servers.get_sales(data=data,db=db)

@router.post("/", response_model=SaleCreate)
def create_sale(data:SaleCreate,db:Session=Depends(get_db)):

    return sale_servers.create_sale(data=data , db=db)

@router.put("/{sale_id}",response_model=SalesRespones)
def update_sale(sale_id:int,data:SalesRespones, db:Session=Depends(get_db)):
    return sale_servers.update_sale(sale_id=sale_id, data=data,db=db)

@router.delete("/{sale_id}",response_model=SalesRespones)
def delete_sale(sale_id:int, db:Session=Depends(get_db)):
    return sale_servers.delete_sale(sale_id=sale_id, db=db)