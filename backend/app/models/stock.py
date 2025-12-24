from pydantic import BaseModel

class Stock(BaseModel):
    symbol: str
    name: str
    price: float
    volatility: float
    annual_return: float
    market_cap: float
    