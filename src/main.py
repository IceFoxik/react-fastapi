from fastapi import FastAPI
from src.config import settings
from src.http_client import CMCHTTPCLIENT

app = FastAPI()

cmc_client = CMCHTTPCLIENT(
    base_url="https://pro-api.coinmarketcap.com",
    api_key=settings.API_KEY
)

@app.get("/cryptocurrencies")
async def get_cryptocurrencies():
    return await cmc_client.get_listings

@app.get("/cryptocurrencies/{currency_id}")
async def get_cryptocurrencies(currency_id: int):
    return await cmc_client.get_currency(currency_id)