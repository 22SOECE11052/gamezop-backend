from fastapi import FastAPI, HTTPException
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

GAMEZOP_TOKEN = os.getenv("GAMEZOP_TOKEN")

app = FastAPI(title="Gamezop API Proxy")

@app.get("/")
def root():
    return {"status": "API is running"}

@app.get("/games")
async def get_games(lang: str = "en"):
    url = "https://api.gamezop.com/v3/games"
    headers = {
        "Authorization": f"Bearer {GAMEZOP_TOKEN}"
    }
    params = {"lang": lang}

    async with httpx.AsyncClient() as client:
        response = await client.get(url, headers=headers, params=params)

    if response.status_code != 200:
        raise HTTPException(
            status_code=response.status_code,
            detail=response.text
        )

    return response.json()
