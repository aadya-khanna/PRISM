from fastapi import FastAPI
from app.routers import stock

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}

app.include_router(stock.router)
