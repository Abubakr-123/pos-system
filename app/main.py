from fastapi import FastAPI
from app.backend.database.database import Base ,engine



Base.metadata.create_all(bind=engine)
app=FastAPI(title="pos test")


@app.get("/")
def home():
    return{"massge":"hello from first projct"}

