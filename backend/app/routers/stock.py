from fastapi import APIRouter
from app.models.stock import Stock

router = APIRouter(prefix="/stocks")

@router.get("/discover", response_model=list[Stock])
def discover_stocks():
    return [
        Stock(
            symbol="AAPL",
            name="Apple",
            price=190,
            volatility=0.22,
            annual_return=0.18,
            market_cap=3e12
        )
    ]
