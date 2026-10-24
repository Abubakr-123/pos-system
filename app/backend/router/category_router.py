from fastapi import APIRouter , Depends 
from sqlalchemy.orm import Session
from app.backend.database.database import get_db
from app.backend.servers import category_server
from app.backend.schema.careogry import CategoryCreate ,CategoryRespones


router=APIRouter(prefix="/Category",tags=["categorys"])

@router.get("/",response_model=list[CategoryRespones])
def get_category(data:CategoryRespones,db:Session=Depends(get_db)):
    return category_server.get_category(data=data,db=db)

@router.post("/",response_model=CategoryCreate)
def create_category(data:CategoryCreate, db:Session=Depends(get_db)):
    return category_server.create_category(data=data,db=db)

@router.put("/{category_id}",response_model=CategoryRespones)
def update_category(cate_id:int,data:CategoryRespones,db:Session=Depends(get_db)):
    return category_server.update_category(cate_id=cate_id,data=data,db=db)

@router.delete("/{category_id}",response_model=CategoryRespones)
def delete_category(cate_id:int,db:Session=Depends(get_db)):
    return category_server.delete_category(cate_id=cate_id, db=db)