from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sqlalchemy.orm import Session
from src.shared.database.session import get_db
from src.shared.database.models import Conversation, Message
from src.shared.types.chat import ChatMessageRequest, ChatResponse, MessageResponse
from src.features.ai.graph import create_agent_graph
from langchain_core.messages import HumanMessage

app = FastAPI(
    title="Telecom AI Assistant API",
    version="1.0.0",
    description="Backend API for the AI Telecom Assistant",
)

# CORS setup for frontend development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class HealthResponse(BaseModel):
    status: str
    version: str

@app.get("/api/v1/health", response_model=HealthResponse)
async def health_check() -> HealthResponse:
    """Minimal health check endpoint for infrastructure verification."""
    return HealthResponse(status="ok", version="1.0.0")

# Initialize the AI Agent Graph
ai_agent = create_agent_graph()

@app.post("/api/v1/chat", response_model=ChatResponse)
async def chat(request: ChatMessageRequest, db: Session = Depends(get_db)):
    """
    Chat endpoint that runs the query through the LangGraph agent.
    """
    # 1. Get or create conversation
    conv_id = request.conversation_id
    if conv_id is None:
        new_conv = Conversation(user_id="guest_user")
        db.add(new_conv)
        db.commit()
        db.refresh(new_conv)
        conv_id = new_conv.id
    else:
        conv = db.query(Conversation).filter(Conversation.id == conv_id).first()
        if not conv:
            raise HTTPException(status_code=404, detail="Conversation not found")
        conv_id = conv.id

    # 2. Prepare state for the AI Agent
    # We only pass the current message to minimize token usage as per requirements
    initial_state = {
        "messages": [HumanMessage(content=request.message)],
        "routing_decision": "",
        "context": ""
    }

    # 3. Run the AI Agent
    result = ai_agent.invoke(initial_state)
    # The result is the final state; the last message is the assistant's response
    assistant_response = result["messages"][-1].content

    # 4. Persist messages to DB
    user_msg = Message(conversation_id=conv_id, role="user", content=request.message)
    assistant_msg = Message(conversation_id=conv_id, role="assistant", content=assistant_response)
    db.add_all([user_msg, assistant_msg])
    db.commit()

    # 5. Return conversation history
    all_messages = db.query(Message).filter(Message.conversation_id == conv_id).all()

    return ChatResponse(
        conversation_id=conv_id,
        messages=[
            MessageResponse(role=m.role, content=m.content, created_at=m.created_at)
            for m in all_messages
        ]
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
