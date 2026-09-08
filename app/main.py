from fastapi import FastAPI
from app.backend.router import sale_router , product_router , category_router


app=FastAPI(title="pos test")

@app.get("/")
def home():
    return{"massge":"hello from first projct"}

app.include_router(product_router.router)
app.include_router(sale_router.router)
app.include_router(category_router.router)