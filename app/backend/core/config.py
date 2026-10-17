from fastapi import HTTPException , Depends , status
from datetime import datetime ,timedelta ,timezone
from app.backend.database.database import get_db
from sqlalchemy.orm import Session
from app.backend.models.user import User
from fastapi.security import OAuth2PasswordBearer
from jose import jwt , JWTError
from dotenv import load_dotenv
from app.backend.scheam.user import TokenDate
import os

load_dotenv()

oauth_schema2=OAuth2PasswordBearer(tokenUrl="/login")

SECRET_KEY=os.getenv("SECRET_KEY") 
ALGORTHEM=os.getenv("ALGORTHEM")
ACSESS_TOKEN_MINTETS=30 

def craeate_access_token(data:dict,expier_delta:timedelta | None=None):
    to_encode=data.copy()
    if expier_delta:
        expier=datetime.now(timezone.utc)+ expier_delta
    else:
        expier=datetime.now(timezone.utc)+ timedelta(minutes=15)
    to_encode.update({"exp":expier})
    token=jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORTHEM)
    return token

async def get_current_user(db:Session=Depends(get_db),token:str=Depends(oauth_schema2)):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORTHEM])
        username=payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401,detail="invaled token")
        token_data=TokenDate(username)
    except:
        raise HTTPException(status_code=401,detail="invaled token")
    user=db.query(User).filter(User.name==username)
    if user is None:
        raise HTTPException(status_code=404, detail="not found")
    