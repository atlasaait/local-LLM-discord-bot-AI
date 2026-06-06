from fastapi import APIRouter
from pydantic import BaseModel
from services.llm_service import ask_llm

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@router.post("/chat")
async def chat(request: ChatRequest) -> ChatResponse:
    response = await ask_llm(request.message)
    return ChatResponse(response=response)