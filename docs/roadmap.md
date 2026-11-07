# Project Roadmap

## MVP Goal
Establish a reliable, context-aware AI assistant capable of handling basic telecom queries and escalating to humans.

## Vertical Development Slices

### Slice 1: The Thin Foundation (Infrastructure)
- **Objective:** Validate the end-to-end deployment and communication pipeline.
- **Frontend Scope:** Basic landing page with a "Connect" status indicator.
- **API Scope:** Health check endpoint (`/api/v1/health`).
- **Database Scope:** Basic connection test.
- **Definition of Done:** Frontend deployed on Vercel, Backend on Render, and health check returns `200 OK`.

### Slice 2: Conversation Interface (UI/UX)
- **Objective:** Implement the chat UI and basic message streaming.
- **Frontend Scope:** Chat window, message bubbles, input field.
- **API Scope:** `/api/v1/chat` endpoint (echo mode for now).
- **Database Scope:** Conversation and Message tables.
- **Definition of Done:** User can send a message and receive a response in the UI.

### Slice 3: Core AI Orchestration (Intelligence)
- **Objective:** Integrate LangGraph to route queries.
- **Frontend Scope:** Loading states for AI thinking.
- **API Scope:** Integration of the router agent.
- **Database Scope:** Persistence of agent state.
- **Definition of Done:** AI correctly identifies if a query is about "Billing" vs "Network".

### Slice 4: Telecom Knowledge Base (RAG)
- **Objective:** Provide accurate plan and service information.
- **Frontend Scope:** Citations/Source links in chat.
- **API Scope:** Vector database integration and retrieval logic.
- **Database Scope:** Document embeddings.
- **Definition of Done:** AI answers a specific question about a data plan using a provided document.

### Slice 5: Billing & Account Integration (Secure Data)
- **Objective:** Handle authenticated account queries.
- **Frontend Scope:** User profile and account summary view.
- **API Scope:** Integration with Supabase Auth and account APIs.
- **Database Scope:** User-account relationship mapping.
- **Definition of Done:** User can ask "What is my current balance?" and receive a correct answer.

### Slice 6: Human Escalation (Handoff)
- **Objective:** Seamless transition to a human agent.
- **Frontend Scope:** "Connecting to agent..." UI and agent-specific chat.
- **API Scope:** Ticket creation logic and agent notification.
- **Database Scope:** Case/Ticket management.
- **Definition of Done:** AI triggers an escalation and a human agent sees the conversation history.
