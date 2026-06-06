import fastapi
import uvicorn
import httpx
from fastapi import FastAPI
from route.chat import router as chat_router

app = FastAPI()

app.include_router(chat_router)

@app.get("/")
async def root():
    return {"status": "API en ligne"}