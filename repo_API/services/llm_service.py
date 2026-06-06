import httpx
from config import OLLAMA_URL, MODEL_NAME, SYSTEM_PROMPT_PATH

def load_system_prompt():
    with open(SYSTEM_PROMPT_PATH, "r", encoding="utf-8") as f:
        return f.read()

async def ask_llm(user_message: str) -> str:
    system_prompt = load_system_prompt()
    
    payload = {
        "model": MODEL_NAME,
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        "stream": False
    }
    
    async with httpx.AsyncClient(timeout=150.0) as client:
        response = await client.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        data = response.json()
        return data["message"]["content"]