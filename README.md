# AI Chatbot

A modern, full-stack AI Chatbot application built with Python, FastAPI, and OpenRouter.

## Features

- Real-time chat interface with AI responses
- FastAPI backend with RESTful chat endpoints
- Clean, responsive frontend with vanilla HTML/CSS/JS
- Conversation history and session management
- Environment-based configuration
- Easy deployment and setup

## Project Structure

```
├── README.md
├── requirements.txt
├── .env.example
├── .gitignore
├── app/
│   ├── __init__.py
│   ├── main.py          # FastAPI application and routes
│   ├── models.py        # Pydantic request/response models
│   └── chat.py          # Chat service with LLM integration
└── frontend/
    ├── index.html       # Chat UI
    ├── style.css        # Styling
    └── app.js           # Frontend chat logic
```

## Getting Started

### Prerequisites

- Python 3.9+
- An OpenRouter API key (https://openrouter.ai/keys)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Zaluxic/Vibe-Coding.git
   cd Vibe-Coding
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables:
   ```bash
   cp .env.example .env
   # Edit .env and add your OPENROUTER_API_KEY
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Open your browser to http://localhost:8000

## API Endpoints

- `GET /` - Serve the frontend chat interface
- `POST /api/chat` - Send a message and get an AI response
- `GET /api/health` - Health check

### POST /api/chat

Request:
```json
{
  "message": "Hello, how are you?",
  "session_id": "optional-session-id"
}
```

Response:
```json
{
  "response": "I'm doing well, thank you! How can I help you today?",
  "session_id": "optional-session-id"
}
```

## Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENROUTER_API_KEY` | Your OpenRouter API key | Yes |
| `OPENROUTER_MODEL` | Model to use (default: openrouter/auto) | No |
| `OPENROUTER_BASE_URL` | OpenRouter API base URL (default: https://openrouter.ai/api/v1) | No |
| `PORT` | Server port (default: 8000) | No |

## License

MIT License
