from jose import jwt 
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime , timedelta ,timezone
from fastapi import Depends ,HTTPException , status
from app.backend.database.database import get_db
from sqlalchemy.orm import Session
from app.backend.models.user import User
import os
load_dotenv()

SECRET_KEY=os.getenv("SECRET_KEY")
ALGORTHEM=os.getenv("ALGORTHEM")
ACCSESS_EXPIER_MINETS=os.getenv("ACCSESS_EXPIER_MINETS")      

oauth_schema2=OAuth2PasswordBearer(tokenUrl="/login")

def create_token(user_id):
    expire=datetime.now(timezone.utc)+timedelta(minutes=30)
    payload={
        "sub":str(user_id),
        "exp":expire
    }
    token=jwt.encode(payload,SECRET_KEY,algorithm=[ALGORTHEM])
    return token
def cuurrrt_user(db:Session=Depends(get_db),token:str=Depends(oauth_schema2)):
    try :
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORTHEM])
        user_id=int(payload["sub"])
    except:
        raise HTTPException(status_code=401,detail="invaled token")
    user=db.query(User).filter(User.id==user_id).first()
    if not user:
        raise HTTPException (status_code=401,detail="invaled user")
    return user
