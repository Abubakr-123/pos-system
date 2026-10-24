from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session 
from app.backend.database.database import get_db
from app.backend.schema.product_s import ProductCreate , ProductRespones 
from app.backend.models.product import Product
from app.backend.servers import product_server

router=APIRouter(prefix="/product",tags=["products"])


@router.get("/", response_model=list[ProductRespones])
def get_product(data:ProductRespones,db:Session=Depends(get_db)):
    return product_server.get_porduct(data=data,db=db)


@router.post("/",response_model=ProductCreate)
def creata_product(data:ProductCreate,db:Session=Depends(get_db)):
    return product_server.create_product(data=data,db=db)


@router.put("/{product_id}",response_model=ProductRespones)
def update_product(product_id:int,data:ProductRespones,db:Session=Depends(get_db)):
    return product_server.update_product(data=data,db=db,product_id=product_id)
    

@router.delete("/{product_id}",response_model=ProductRespones)
def delete_product(product_id:int,db:Session=Depends(get_db)):
    return product_server.delete_product(product_id=product_id,db=db)