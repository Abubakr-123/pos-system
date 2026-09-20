from app.backend.models.user import User , UserRole
from app.backend.schema.user import UserRespones , UsersCreate , UserLogin
from sqlalchemy.orm import Session
from app.backend.core.security import hash_password ,verify_password
from fastapi import HTTPException , status
from app.backend.core.config import currnet_user

def login(db:Session,data:UserLogin):
    # verify_pass=verify_password(data.password,)
    user=db.query(User).filter(User.username==data.username).first()
    if user:
       # raise HTTPException(status_code=status.HTTP_302_FOUND,detail="invaled password")
        if not verify_password(data.password,user.hash_password):
          raise HTTPException(status_code=status.HTTP_302_FOUND,detail="invaled password")
    return user

    

def get_user(data:UserRespones,db:Session):
    user=db.query(User).all()
    return user

def create_user(data:UsersCreate,db:Session):
    hashed_password=hash_password(data.hash_password)
    user=db.query(User).filter(User.username==data.username).first()
    if user:
        raise HTTPException(status_code=status.HTTP_302_FOUND,detail="user alredy exist")
    new_user=User(
        username=data.username,
        hash_password=hashed_password
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
def update_user(user_id:int,data:UserRespones,db:Session):
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    update_data=data.model_dump(exclude_unset=True)
    for key , value in update_data.items:
        setattr( user , key , value)
    db.commit()
    db.refresh(user)
    return user

def delete_user(user_id:int, data:UserRespones,db:Session):
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException(status_code=404,detail="user not found")
    db.delete(user)