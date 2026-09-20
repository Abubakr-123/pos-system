
from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from app.backend.schema.user import UserRespones , UsersCreate ,UserLogin
from app.backend.database.database import get_db
from app.backend.servers import user_servirs


router=APIRouter(prefix="/User",tags=["users"])

@router.post("/login",response_model=UserRespones)
def login(data:UserLogin,db:Session=Depends(get_db)):
    return user_servirs.login(data=data, db=db)


@router.get("/",response_model=list[UserRespones])
def get_user(data:UserRespones,db:Session=Depends(get_db)):
    return user_servirs.get_user(data=data,db=db)

@router.post("/",response_model=UsersCreate)
def create_user(data:UsersCreate,db:Session=Depends(get_db)):
    return user_servirs.create_user(data=data,db=db)

@router.put("/{user_id}",response_model=UserRespones)
def update_user(user_id:int,data:UserRespones,db:Session=Depends(get_db)):
    return user_servirs.update_user(user_id=user_id,data=data,db=db)

@router.delete("/{user_id}",response_model=UserRespones)
def delete_user(user_id:int,db:Session=Depends(get_db)):
    return user_servirs.delete_user(user_id=user_id,db=db)

