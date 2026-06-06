from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
OLLAMA_URL = "http://127.0.0.1:11434/api/chat"
MODEL_NAME = "llama3.2:1b"
SYSTEM_PROMPT_PATH = BASE_DIR / "repo_LLM" / "system_prompt.txt"