from fastapi import HTTPException , Depends , status
from datetime import datetime ,timedelta ,timezone
from app.backend.database.database import get_db
from sqlalchemy.orm import Session
from app.backend.models.user import User , UserRole
from fastapi.security import OAuth2PasswordBearer
from jose import jwt , JWTError
from dotenv import load_dotenv
from app.backend.schema.user import Token 
import os

load_dotenv()

oauth_schema2=OAuth2PasswordBearer(tokenUrl="/login")

SECRET_KEY=os.getenv("SECRET_KEY") 
ALGORTHEM=os.getenv("ALGORTHEM")
ACSESS_TOKEN_MINTETS=30 

def create_token(user_id:int,token_type:str,expires:timedelta)->str:
    payload={
        "sub":str(user_id),
        "type":token_type,
        "exp":datetime.now(timezone.utc())+timedelta(minutes=15)
    }
    return jwt.encode(payload , SECRET_KEY , algorithm=ALGORTHEM)
#انشاء التوكن
def access_token(user_id:int):
    return create_token(user_id ,"access", timedelta(minutes=15))
#تحديث التوكن
def refresh_tkoen(user_id:int ):
    return create_token(user_id,"refresh",timedelta(days=7))
#فك تشفير التوكن
def decode_token(token:str,expected:str):
    try:
        payload=jwt.decode(token,SECRET_KEY, algorithms=[ALGORTHEM])
        if payload.get("type")!=expected:
            raise ValueError
        return int(payload.get["sub"])
    except:
        raise 
    #التحقق من المستخدم
def get_current_user(token:str=Depends(oauth_schema2),db:Session=Depends(get_db))->User:
    user_id=decode_token(token , "access")
    user=db.get(User , user_id)
    if user is None:
        raise
    return user
#التحقق من صلاحية المستخدم
def require_admin(user:User=Depends(get_current_user))->User:
    if user.role!=UserRole.MANAGER:
        raise
    
    
