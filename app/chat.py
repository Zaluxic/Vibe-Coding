import os
from typing import Optional, Dict, List
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class ChatService:
    def __init__(self):
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.model = os.getenv("OPENROUTER_MODEL", "openrouter/auto")
        self.base_url = os.getenv("OPENROUTER_BASE_URL", "https://openrouter.ai/api/v1")
        self.client = None
        if self.api_key:
            self.client = OpenAI(
                api_key=self.api_key,
                base_url=self.base_url,
            )
        self.sessions: Dict[str, List[dict]] = {}

    def get_session_messages(self, session_id: Optional[str]) -> List[dict]:
        if session_id and session_id in self.sessions:
            return self.sessions[session_id]
        return []

    def save_session_messages(self, session_id: Optional[str], messages: List[dict]):
        if session_id:
            self.sessions[session_id] = messages[-20:]  # Keep last 20 messages

    async def get_response(self, message: str, session_id: Optional[str] = None) -> str:
        if not self.client:
            return "I'm sorry, the OpenRouter API key is not configured. Please set OPENROUTER_API_KEY in your environment variables."

        history = self.get_session_messages(session_id)

        messages = [
            {
                "role": "system",
                "content": "You are a helpful, friendly AI assistant. Keep your responses concise and conversational.",
            }
        ]
        messages.extend(history)
        messages.append({"role": "user", "content": message})

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=0.7,
                max_tokens=500,
            )
            ai_response = response.choices[0].message.content or "I'm sorry, I couldn't generate a response."

            # Update conversation history
            history.append({"role": "user", "content": message})
            history.append({"role": "assistant", "content": ai_response})
            self.save_session_messages(session_id, history)

            return ai_response
        except Exception as e:
            return f"I'm sorry, I encountered an error: {str(e)}"


chat_service = ChatService()
