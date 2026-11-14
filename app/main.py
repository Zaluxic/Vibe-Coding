from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from app.models import ChatMessage, ChatResponse, HealthResponse
from app.chat import chat_service
from datetime import datetime
import os

app = FastAPI(title="AI Chatbot", version="1.0.0")

BASE_DIR = Path(__file__).resolve().parent.parent
FRONTEND_DIR = BASE_DIR / "frontend"

# Mount static files
app.mount("/static", StaticFiles(directory=str(FRONTEND_DIR)), name="static")


def get_timestamp() -> str:
    return datetime.utcnow().isoformat() + "Z"


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    """Serve the chat frontend."""
    html_path = FRONTEND_DIR / "index.html"
    return HTMLResponse(content=html_path.read_text(), status_code=200)


@app.post("/api/chat", response_model=ChatResponse)
async def chat(chat_msg: ChatMessage):
    """Send a message and get an AI response."""
    response_text = await chat_service.get_response(chat_msg.message, chat_msg.session_id)
    return ChatResponse(
        response=response_text,
        session_id=chat_msg.session_id,
        timestamp=get_timestamp(),
    )


@app.get("/api/health", response_model=HealthResponse)
async def health():
    """Health check endpoint."""
    return HealthResponse(status="healthy", timestamp=get_timestamp())


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app,
        host=os.getenv("HOST", "0.0.0.0"),
        port=int(os.getenv("PORT", "8000")),
    )
