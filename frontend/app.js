const messageInput = document.getElementById('messageInput');
const sendBtn = document.getElementById('sendBtn');
const chatForm = document.getElementById('chatForm');
const messagesContainer = document.getElementById('messages');
const statusEl = document.getElementById('status');

let sessionId = null;

function addMessage(text, sender, timestamp) {
    const div = document.createElement('div');
    div.className = `message ${sender}`;
    div.textContent = text;
    messagesContainer.appendChild(div);
    messagesContainer.scrollTop = messagesContainer.scrollHeight;
}

function setStatus(text, type = '') {
    statusEl.textContent = text;
    statusEl.className = `status ${type}`;
}

function setLoading(loading) {
    sendBtn.disabled = loading;
    messageInput.disabled = loading;
    if (loading) {
        setStatus('AI is typing...', 'typing');
    } else {
        setStatus('');
    }
}

async function sendMessage() {
    const text = messageInput.value.trim();
    if (!text) return;

    addMessage(text, 'user');
    messageInput.value = '';
    setLoading(true);

    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                message: text,
                session_id: sessionId,
            }),
        });

        const data = await response.json();
        sessionId = data.session_id;
        addMessage(data.response, 'ai');
    } catch (error) {
        console.error(error);
        addMessage('Sorry, something went wrong. Please try again.', 'ai');
    } finally {
        setLoading(false);
    }
}

chatForm.addEventListener('submit', (e) => {
    e.preventDefault();
    sendMessage();
});

messageInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        e.preventDefault();
        sendMessage();
    }
});

// Welcome message
addMessage('Hello! I\'m your AI assistant. How can I help you today?', 'ai');
